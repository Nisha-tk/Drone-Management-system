from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.schemas.survey_area import SurveyAreaCreate, SurveyAreaResponse , SurveyAreaUpdate
from src.services.survey_area import SurveyAreaService
from src.schemas.response import SuccessResponse, PaginatedResponse, PaginationMeta
from src.utils.dependencies import allowed_roles
from src.enums.user_role   import UserRole

survey_area_router = APIRouter(prefix="/survey-areas", tags=["Survey Areas"])

@survey_area_router.post(
    "",
    response_model=SuccessResponse[SurveyAreaResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR]))],
)
def create_survey_area(payload: SurveyAreaCreate, db: Session = Depends(get_db)):
    area = SurveyAreaService.create(db, payload)
    return SuccessResponse(data=area)

@survey_area_router.get(
    "",
    response_model=PaginatedResponse[SurveyAreaResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR]))],
)
def list_survey_areas(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
):
    areas, total = SurveyAreaService.list(db, page, page_size)
    return PaginatedResponse(
        data=areas,
        meta=PaginationMeta(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=(total + page_size - 1) // page_size,
        ),
    )

@survey_area_router.put(
    "/{area_id}",
    response_model=SuccessResponse[SurveyAreaResponse],
    dependencies=[Depends(allowed_roles([UserRole.ADMIN]))],
)
def update_survey_area(
    area_id: str,
    payload: SurveyAreaUpdate,
    db: Session = Depends(get_db),
):
    area = SurveyAreaService.update(db, area_id, payload)
    return SuccessResponse(data=area)
