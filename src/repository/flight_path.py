from sqlalchemy.orm import Session
from src.models.flight_path import FlightPaths

class FlightPathRepository:

    @staticmethod
    def create(db: Session, path: FlightPaths) -> FlightPaths:
        db.add(path)
        db.commit()
        db.refresh(path)
        return path

    @staticmethod
    def get_by_mission(db: Session, mission_id):
        return (
            db.query(FlightPaths)
            .filter(FlightPaths.mission_id == mission_id)
            .first()
        )
    
