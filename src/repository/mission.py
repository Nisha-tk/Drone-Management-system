from sqlalchemy.orm import Session
from typing import Tuple, List
from src.models.mission import Missions

class MissionRepository:

    @staticmethod
    def create(db: Session, mission: Missions) -> Missions:
        db.add(mission)
        db.commit()
        db.refresh(mission)
        return mission

    @staticmethod
    def get_by_id(db: Session, mission_id):
        return db.query(Missions).filter(Missions.id == mission_id).first()

    @staticmethod
    def list_by_operator(
        db: Session,
        operator_id,
        skip: int,
        limit: int,
    ) -> Tuple[List[Missions], int]:
        query = db.query(Missions).filter(Missions.operator_id == operator_id)
        total = query.count()
        return query.offset(skip).limit(limit).all(), total

    @staticmethod
    def list_all(
        db: Session,
        skip: int,
        limit: int,
    ) -> Tuple[List[Missions], int]:
        query = db.query(Missions)
        total = query.count()
        return query.offset(skip).limit(limit).all(), total
    @staticmethod
    def update(db: Session, mission: Missions, data: dict) -> Missions:
        for key, value in data.items():
            setattr(mission, key, value)
        db.commit()
        db.refresh(mission)
        return mission


    @staticmethod
    def delete(db: Session, mission: Missions) -> None:
        db.delete(mission)
        db.commit()

