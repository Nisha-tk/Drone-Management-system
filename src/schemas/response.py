from pydantic import BaseModel
from typing import Optional, List, TypeVar, Generic


T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    status: str = "success"
    message: Optional[str] = "Successfully data fetched"
    data: T

    class Config:
        from_attributes = True   


class PaginationMeta(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    status: str = "success"
    message: Optional[str] = "Records successfully fetched!"
    data: List[T]
    meta: PaginationMeta

    class Config:
        from_attributes = True




class FieldError(BaseModel):
    field: str
    message: str


class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    errors: Optional[List[FieldError]] = None
