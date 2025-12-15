from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.flight_path import FlightPaths
from src.repository.flight_path import FlightPathRepository
from src.repository.mission import MissionRepository
from src.exceptions.app_exceptions import (
    NotFoundException,
    ConflictException,
    DatabaseException,
)
from src.constants.error_messages import ErrorMessages


class FlightPathService:

    @staticmethod
    def create(db: Session, payload):
        if not db:
            raise DatabaseException(ErrorMessages.DB_SESSION_MISSING)

        try:
            mission = MissionRepository.get_by_id(db, payload.mission_id)
            if not mission:
                raise NotFoundException(ErrorMessages.MISSION_NOT_FOUND)

            existing = FlightPathRepository.get_by_mission(db, payload.mission_id)
            if existing:
                raise ConflictException(ErrorMessages.FLIGHT_PATH_ALREADY_EXISTS)

            path = FlightPaths(
                mission_id=payload.mission_id,
                pattern_type=payload.pattern_type,
                waypoints=payload.waypoints,
            )

            return FlightPathRepository.create(db, path)

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )
