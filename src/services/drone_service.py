from sqlalchemy.orm import Session
from src.models.drone import Drones
from src.repository.drone import DroneRepository
from src.constants.error_messages import ErrorMessages
from src.exceptions.app_exceptions import NotFoundException , DatabaseException
from sqlalchemy.exc import SQLAlchemyError

class DroneService:

    @staticmethod
    def create_drone(db: Session, payload):
        drone = Drones(
            name=payload.name,
            model=payload.model,
        )
        return DroneRepository.create(db, drone)

    @staticmethod
    def list_drones(
    db: Session,
    page: int,
    page_size: int,
    name: str | None,
):
        
        if not db:
            raise DatabaseException(ErrorMessages.DB_SESSION_MISSING)

        try:
            skip = (page - 1) * page_size

            drones, total = DroneRepository.list(
                db=db,
                skip=skip,
                limit=page_size,
                name=name,
            )

            return drones, total

        except SQLAlchemyError as e:
            
            raise DatabaseException(ErrorMessages.DB_OPERATION_FAILED)


    @staticmethod
    def get_drone(db: Session, drone_id):
        drone = DroneRepository.get_by_id(db, drone_id)
        if not drone:
            raise NotFoundException(ErrorMessages.DRONE_NOT_FOUND)
        return drone
    
    @staticmethod
    def update_drone(db: Session, drone_id, payload):
        if not db:
            raise DatabaseException(ErrorMessages.DB_SESSION_MISSING)

        try:
            drone = DroneRepository.get_by_id(db, drone_id)
            if not drone:
                raise NotFoundException(ErrorMessages.DRONE_NOT_FOUND)

            updated = DroneRepository.update(
                db,
                drone,
                payload.model_dump(exclude_unset=True),
            )
            return updated

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )
        

    @staticmethod
    def delete_drone(db: Session, drone_id):
        if not db:
            raise DatabaseException(ErrorMessages.DB_SESSION_MISSING)

        try:
            drone = DroneRepository.get_by_id(db, drone_id)
            if not drone:
                raise NotFoundException(ErrorMessages.DRONE_NOT_FOUND)

            DroneRepository.delete(db, drone)
            return None

        except SQLAlchemyError as e:
            raise DatabaseException(
                ErrorMessages.DB_OPERATION_FAILED,
                detail=str(e),
            )


