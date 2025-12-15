from fastapi import HTTPException, status


class AppException(HTTPException):
    """Base custom application exception."""
    def __init__(self, message: str, status_code: int = 400, detail: str = None):
        super().__init__(status_code=status_code, detail=message)
        self.error_detail = detail


class NotFoundException(AppException):
    def __init__(self, message="Resource not found", detail=None):
        super().__init__(message, status_code=404, detail=detail)


class ConflictException(AppException):
    def __init__(self, message="Conflict occurred", detail=None):
        super().__init__(message, status_code=409, detail=detail)


class ValidationException(AppException):
    def __init__(self, message="Validation error", detail=None):
        super().__init__(message, status_code=422, detail=detail)



class DatabaseException(AppException):
    def __init__( self,message="Database operation failed",detail=None,):
        super().__init__(
            message=message,
            status_code=500,
            detail=detail,
        )




