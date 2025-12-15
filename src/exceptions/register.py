from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.schemas.response import ErrorResponse, FieldError


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = []

        for err in exc.errors():
            field = ".".join(str(x) for x in err.get("loc", []) if isinstance(x, str))
            message = err.get("msg")

            errors.append(FieldError(field=field, message=message))

        response = ErrorResponse(
            message="Validation error",
            errors=errors
        )

        return JSONResponse(
            status_code=422,
            content=response.model_dump()
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):

        response = ErrorResponse(
            message=exc.detail,
            errors=[FieldError(field="general", message=exc.detail)]
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump()
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):

        response = ErrorResponse(
            message="Internal server error",
            errors=[FieldError(field="server", message=str(exc))]
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump()
        )
