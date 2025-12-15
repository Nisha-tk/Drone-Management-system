from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.repository.mission import MissionRepository
from src.repository.drone import DroneRepository
from src.repository.survey_area import SurveyAreaRepository
from src.models.mission import Missions
from src.exceptions.app_exceptions import DatabaseException , NotFoundException
from src.constants.error_messages import ErrorMessages
from src.enums.user_role import UserRole

class MissionService:

    @staticmethod
    def create(
        db: Session,
        payload,
        operator_id,
    ):
        try:
            drone = DroneRepository.get_by_id(db, payload.drone_id)
            if not drone:
                raise NotFoundException(ErrorMessages.DRONE_NOT_FOUND)

            area = SurveyAreaRepository.get_by_id(db, payload.survey_area_id)
            if not area:
                raise NotFoundException(ErrorMessages.SURVEY_AREA_NOT_FOUND)

            mission = Missions(
                drone_id=payload.drone_id,
                operator_id=operator_id,
                survey_area_id=payload.survey_area_id,
                altitude=payload.altitude,
                overlap_percentage=payload.overlap_percentage,
                sensor_type=payload.sensor_type,
                data_collection_frequency=payload.data_collection_frequency,
            )

            return MissionRepository.create(db, mission)

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )

    @staticmethod
    def list(
        db: Session,
        current_user,
        page: int,
        page_size: int,
    ):
        try:
            skip = (page - 1) * page_size

            if current_user.role == UserRole.ADMIN:
                return MissionRepository.list_all(db, skip, page_size)

            return MissionRepository.list_by_operator(
                db, current_user.id, skip, page_size
            )

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )
        
    @staticmethod
    def get_by_id(db: Session, mission_id, current_user):
        mission = MissionRepository.get_by_id(db, mission_id)

        if not mission:
            raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

        if (
            current_user.role != UserRole.ADMIN
            and mission.operator_id != current_user.id
        ):
            raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

        return mission
    
    @staticmethod
    def update(
        db: Session,
        mission_id,
        payload,
        current_user,
    ):
        try:
            mission = MissionRepository.get_by_id(db, mission_id)
            if not mission:
                raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

            if (
                current_user.role != UserRole.ADMIN
                and mission.operator_id != current_user.id
            ):
                raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

            return MissionRepository.update(
                db,
                mission,
                payload.model_dump(exclude_unset=True),
            )

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )

    @staticmethod
    def delete(
        db: Session,
        mission_id,
        current_user,
    ):
        try:
            mission = MissionRepository.get_by_id(db, mission_id)
            if not mission:
                raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

            if current_user.role != UserRole.ADMIN:
                raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

            MissionRepository.delete(db, mission)

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )
