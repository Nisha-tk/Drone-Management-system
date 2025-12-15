from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.schemas.flight_path import FlightPathCreate, FlightPathResponse
from src.schemas.response import SuccessResponse
from src.services.flight_path_service import FlightPathService
from src.utils.dependencies import allowed_roles
from src.enums.user_role import UserRole

flight_router = APIRouter(
    prefix="/flight-paths",
    tags=["Flight Paths"],
)

@flight_router.post(
    "",
    response_model=SuccessResponse[FlightPathResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR]))],
)
def create_flight_path(
    payload: FlightPathCreate,
    db: Session = Depends(get_db),
):
    path = FlightPathService.create(db, payload)
    return SuccessResponse(data=path)
