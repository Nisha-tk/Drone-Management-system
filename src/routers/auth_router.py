from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.schemas.auth import LoginSchema, LoginResponse
from src.schemas.response import SuccessResponse
from src.schemas.user import UserResponse , UserCreate
from src.services.auth_service import AuthService
from src.constants.succes_messages import Messages


auth_router = APIRouter(prefix="/auth", tags=["Auth"])



@auth_router.post("/sign-up",response_model=SuccessResponse[UserResponse])
def sign_up(user : UserCreate, db:Session= Depends(get_db)):
    user = AuthService.sign_up(db, user.model_dump())

    return SuccessResponse(message=Messages.USER_CREATED,data=UserResponse.model_validate(user))



@auth_router.post("/login", response_model=SuccessResponse[LoginResponse])
def login(payload: LoginSchema, db: Session = Depends(get_db)):

    access_token  = AuthService.login(
        db=db,
        email=payload.email,
        password=payload.password
    )

    return SuccessResponse(
        message=Messages.LOGIN_SUCCESS,
        data=LoginResponse(access_token=access_token)
    )
