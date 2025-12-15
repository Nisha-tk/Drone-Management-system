from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.repository.user_repository import UserRepository
from src.utils.password_manager import PasswordManager
from src.core.secutity import JWTManager
from src.models.users import Users
from src.constants.error_messages import ErrorMessages
from src.schemas.user import UserCreate
from src.enums.user_role import UserRole


class AuthService:



    @staticmethod
    def sign_up(db:Session, user:dict):
        user = UserRepository.get_by_email(db, user["email"])
        if user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=ErrorMessages.EMAIL_ALREADY_EXISTS)
        
        password = PasswordManager.hash_password(user["password"])
        user.update({"password": password})
        user_obj = Users(**user)
        created_user = UserRepository.create(db,user_obj)
        return created_user
        

    @staticmethod
    def login(db: Session, email: str, password: str) -> str:

        user = UserRepository.get_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=ErrorMessages.INVALID_CREDENTIALS
            )

        if not PasswordManager.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=ErrorMessages.INVALID_CREDENTIALS
            )

        access_token = JWTManager.create_access_token(
            {"sub": str(user.id), "role": user.role.value}
        )

        return access_token 
