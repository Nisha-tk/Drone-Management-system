from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mission_report import MissionReports
from src.repository.mission_report import MissionReportRepository
from src.repository.mission import MissionRepository
from src.exceptions.app_exceptions import NotFoundException, ConflictException , DatabaseException
from src.constants.error_messages import ErrorMessages

class MissionReportService:

    @staticmethod
    def create(db: Session, payload):
        try:
            mission = MissionRepository.get_by_id(db, payload.mission_id)
            if not mission:
                raise NotFoundException(ErrorMessages.MISSION_ALREADY_EXISTS)

            existing = MissionReportRepository.get_by_mission(db, payload.mission_id)
            if existing:
                raise ConflictException(ErrorMessages.REPORT_ALREADY_EXISTS)

            report = MissionReports(
                mission_id=payload.mission_id,
                summary=payload.summary,
                total_flight_time=payload.total_flight_time,
                area_covered_sq_m=payload.area_covered_sq_m,
            )

            return MissionReportRepository.create(db, report)

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )
