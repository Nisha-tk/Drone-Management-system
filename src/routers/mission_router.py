from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.schemas.mission import MissionCreate, MissionResponse , MissionUpdate
from src.schemas.response import SuccessResponse, PaginatedResponse, PaginationMeta
from src.services.mission_service import MissionService
from src.utils.dependencies import allowed_roles
from src.enums.user_role import UserRole

mission_router = APIRouter(prefix="/missions", tags=["Missions"])

@mission_router.post(
    "",
    response_model=SuccessResponse[MissionResponse],
)
def create_mission(
    payload: MissionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(allowed_roles([UserRole.OPERATOR])),
):
    mission = MissionService.create(
        db=db,
        payload=payload,
        operator_id=current_user.id,
    )
    return SuccessResponse(data=mission)

@mission_router.get(
    "",
    response_model=PaginatedResponse[MissionResponse],
)
def list_missions(
    db: Session = Depends(get_db),
    current_user=Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR])),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
):
    missions, total = MissionService.list(
        db, current_user, page, page_size
    )

    return PaginatedResponse(
        data=missions,
        meta=PaginationMeta(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=(total + page_size - 1) // page_size,
        ),
    )

@mission_router.get(
    "/{mission_id}",
    response_model=SuccessResponse[MissionResponse],
)
def get_mission(
    mission_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR])),
):
    mission = MissionService.get_by_id(db, mission_id, current_user)
    return SuccessResponse(data=mission)


@mission_router.put(
    "/{mission_id}",
    response_model=SuccessResponse[MissionResponse],
)
def update_mission(
    mission_id: str,
    payload: MissionUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR])),
):
    mission = MissionService.update(
        db=db,
        mission_id=mission_id,
        payload=payload,
        current_user=current_user,
    )
    return SuccessResponse(data=mission)


@mission_router.delete(
    "/{mission_id}",
    response_model=SuccessResponse[None],
)
def delete_mission(
    mission_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(allowed_roles([UserRole.ADMIN])),
):
    MissionService.delete(db, mission_id, current_user)
    return SuccessResponse(
        message="Mission deleted successfully",
        data=None,
    )






