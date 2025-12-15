from fastapi import APIRouter, Depends , Query
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.drone_service import DroneService
from src.schemas.drones import DroneCreate, DroneResponse , DroneUpdate
from src.schemas.response import SuccessResponse , PaginatedResponse , PaginationMeta
from src.utils.dependencies import allowed_roles
from src.enums.user_role import UserRole

drone_router = APIRouter(prefix="/drones", tags=["Drones"])

@drone_router.post(
    "",
    response_model=SuccessResponse[DroneResponse],
   dependencies=[Depends(allowed_roles([UserRole.ADMIN]))]
)
def create_drone(
    payload: DroneCreate,
    db: Session = Depends(get_db)
):
    drone = DroneService.create_drone(db, payload)
    return SuccessResponse(data=drone)


@drone_router.get(
    "/{drone_id}",
    response_model=SuccessResponse[DroneResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR]))],
)
def get_drone(
    drone_id: str,
    db: Session = Depends(get_db),
):
    drone = DroneService.get_drone(db, drone_id)
    return SuccessResponse(data=drone)


@drone_router.get(
    "",
    response_model=PaginatedResponse[DroneResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN,UserRole.OPERATOR]))],
)
def list_drones(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: str | None = Query(None, description="Search drone by name"),
):
    drones, total = DroneService.list_drones(
        db=db,
        page=page,
        page_size=page_size,
        name=name,
    )

    total_pages = (total + page_size - 1) // page_size

    return PaginatedResponse(
        data=drones,
        meta=PaginationMeta(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=total_pages,
        ),
    )



@drone_router.put(
    "/{drone_id}",
    response_model=SuccessResponse[DroneResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN]))],
)
def update_drone(
    drone_id: str,
    payload: DroneUpdate,
    db: Session = Depends(get_db),
):
    drone = DroneService.update_drone(db, drone_id, payload)
    return SuccessResponse(data=drone)


@drone_router.delete(
    "/{drone_id}",
    response_model=SuccessResponse[None],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN]))],
)
def delete_drone(
    drone_id: str,
    db: Session = Depends(get_db),
):
    DroneService.delete_drone(db, drone_id)
    return SuccessResponse(message="Drone deleted successfully", data=None)

