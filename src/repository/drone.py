from sqlalchemy.orm import Session
from src.models.drone import Drones
from typing import Optional , Tuple , List


class DroneRepository:
  
    @staticmethod
    def create(db: Session, drone: Drones) -> Drones:
        db.add(drone)
        db.commit()
        db.refresh(drone)
        return drone

    @staticmethod
    def get_by_id(db: Session, drone_id) -> Drones | None:
        return db.query(Drones).filter(Drones.id == drone_id).first()

    @staticmethod
    def list(
        db: Session,
        skip: int,
        limit: int,
        name: Optional[str] = None,
    ) -> Tuple[List[Drones], int]:

        query = db.query(Drones)

        if name:
            query = query.filter(Drones.name.ilike(f"%{name}%"))

        total = query.count()

        drones = query.offset(skip).limit(limit).all()

        return drones, total

    @staticmethod
    def count(db: Session):
        return db.query(Drones).count()

    @staticmethod
    def update_status(db: Session, drone_id: int, status: str) -> Drones | None:
        drone = DroneRepository.get_by_id(db, drone_id)
        if not drone:
            return None
        drone.status = status
        db.commit()
        db.refresh(drone)
        return drone
    
    @staticmethod
    def update(db: Session, drone, data: dict):
        for key, value in data.items():
            setattr(drone, key, value)
        db.commit()
        db.refresh(drone)
        return drone
    
    @staticmethod
    def delete(db: Session, drone: Drones) -> None:
        db.delete(drone)
        db.commit()
