from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.schemas.mission_report import MissionReportCreate, MissionReportResponse
from src.schemas.response import SuccessResponse
from src.services.mission_report_service import MissionReportService
from src.utils.dependencies import allowed_roles
from src.enums.user_role import UserRole

report_router = APIRouter(prefix="/mission-reports", tags=["Mission Reports"])

@report_router.post(
    "",
    response_model=SuccessResponse[MissionReportResponse],
)
def create_report(
    payload: MissionReportCreate,
    db: Session = Depends(get_db),
    _=Depends(allowed_roles([UserRole.ADMIN, UserRole.OPERATOR, UserRole.VIEWER])),
):
    report = MissionReportService.create(db, payload)
    return SuccessResponse(data=report)
