from sqlalchemy.orm import Session
from src.repository.user_repository import UserRepository
from src.schemas.user import UserCreate, UserOut
from src.exceptions.app_exceptions import (
    ConflictException,
    NotFoundException,
    ValidationException,
)
from src.constants.error_messages import ErrorMessages
from src.utils.password_manager import PasswordManager
from src.models.users import Users


class UserService:

    @staticmethod
    def create_user(db: Session, payload: UserCreate) -> dict:
        

        if db is None:
            raise ValidationException(ErrorMessages.DB_SESSION_MISSING)

        
        if UserRepository.get_by_email(db, payload.email):
            raise ConflictException(ErrorMessages.EMAIL_ALREADY_EXISTS)

        hashed_password = PasswordManager.hash_password(payload.password)

        user = Users(
            name=payload.name,
            email=payload.email,
            password_hash=hashed_password,
            role=payload.role.value,
        )

        created_user = UserRepository.create(db, user)

        return created_user
    



    @staticmethod
    def get_user(db: Session, user_id: int) -> dict:
        

        if db is None:
            raise ValidationException(ErrorMessages.DB_SESSION_MISSING)

        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise NotFoundException(ErrorMessages.USER_NOT_FOUND)

        return user

    @staticmethod
    def list_users(db: Session, page: int, page_size: int) -> tuple[list[dict], int]:
      

        if db is None:
            raise ValidationException(ErrorMessages.DB_SESSION_MISSING)

        skip = (page - 1) * page_size

        total = UserRepository.count(db)
        users = UserRepository.list(db, skip, page_size)

        
        

        return users, total
