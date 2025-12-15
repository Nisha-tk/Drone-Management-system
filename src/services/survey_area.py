from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from src.models.survey_area import SurveyAreas
from src.repository.survey_area import SurveyAreaRepository
from src.exceptions.app_exceptions import DatabaseException , NotFoundException

from src.constants.error_messages import ErrorMessages

class SurveyAreaService:

    @staticmethod
    def create(db: Session, payload):
        try:
            area = SurveyAreas(
                name=payload.name,
                polygon_coordinates=payload.polygon_coordinates,
                total_area_sq_m=payload.total_area_sq_m,
            )
            return SurveyAreaRepository.create(db, area)

        except SQLAlchemyError as e:
            raise DatabaseException(ErrorMessages.DB_OPERATION_FAILED, str(e))

    @staticmethod
    def get(db: Session, area_id):
        area = SurveyAreaRepository.get_by_id(db, area_id)
        if not area:
            raise NotFoundException(ErrorMessages.SURVEY_AREA_NOT_FOUND)
        return area

    @staticmethod
    def list(db: Session, page: int, page_size: int):
        skip = (page - 1) * page_size
        return SurveyAreaRepository.list(db, skip, page_size)
    
    @staticmethod

    def update(db: Session, area_id, payload):
        try:
            area = SurveyAreaRepository.get_by_id(db, area_id)
            if not area:
                raise NotFoundException(ErrorMessages.SURVEY_AREA_NOT_FOUND)

            return SurveyAreaRepository.update(
                db,
                area,
                payload.model_dump(exclude_unset=True),
            )

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )

