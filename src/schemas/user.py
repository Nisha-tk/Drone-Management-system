from pydantic import BaseModel, EmailStr, Field , field_validator 
from uuid import UUID
from src.enums.user_role import UserRole


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=2, max_length=50)
    role: UserRole =   UserRole.VIEWER





class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True
