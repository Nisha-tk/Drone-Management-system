from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError


from fastapi import HTTPException, status

from src.core.config import settings
from src.constants.error_messages import ErrorMessages


class JWTManager:
    SECRET_KEY = settings.JWT_SECRET
    ALGORITHM = settings.JWT_ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    def create_access_token(cls, data: Dict[str, Any], expires_in: Optional[int] = None) -> str:
        """
        Create a JWT access token with expiration.
        """
        

        expire = datetime.now() + timedelta(
            minutes=expires_in or cls.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        data.update({"exp":expire})

        try:
           
            token = jwt.encode(data, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
            
            return token

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.TOKEN_GENERATION_FAILED,
            )

    @classmethod
    def verify_access_token(cls, token: str) -> Dict[str, Any]:
        """
        Verify a JWT token. Raises proper exceptions on failure.
        """
        try:
            payload = jwt.decode(
                token,
                cls.SECRET_KEY,
                algorithms=[cls.ALGORITHM]
            )
            return payload

        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=ErrorMessages.TOKEN_EXPIRED,
                
            )



        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=ErrorMessages.TOKEN_INVALID,
              
            )

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=ErrorMessages.TOKEN_UNKNOWN_ERROR,
            )
