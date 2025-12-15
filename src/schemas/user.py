from pydantic import BaseModel, EmailStr, Field , field_validator 
from uuid import UUID
from src.enums.user_role import UserRole
from src.exceptions.app_exceptions import ValidationException


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=2, max_length=50)
    role: UserRole =   UserRole.VIEWER

    @field_validator("password")
    def validate_password(cls,value):
        check = value.strip()
        if len(check) >= 2:
            return value
        else:
            raise ValidationException(message= "Password shoould be more than 2 characters")
        
   


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True
