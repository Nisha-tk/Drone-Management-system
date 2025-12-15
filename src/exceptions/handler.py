from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from src.schemas.response import ErrorResponse
from src.exceptions.app_exceptions import AppException


def global_handler(message: str, status_code: int, detail: str = None):
    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(
            message=message,
            detail=detail
        ).model_dump()
    )
