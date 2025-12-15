from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    email: str = Field(..., description="User email")
    password: str = Field(..., description="User password")


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
