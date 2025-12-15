from sqlalchemy.orm import Session
from src.models.survey_area import SurveyAreas

class SurveyAreaRepository:

    @staticmethod
    def create(db: Session, area: SurveyAreas):
        db.add(area)
        db.commit()
        db.refresh(area)
        return area

    @staticmethod
    def get_by_id(db: Session, area_id):
        return db.query(SurveyAreas).filter(SurveyAreas.id == area_id).first()

    @staticmethod
    def list(db: Session, skip: int, limit: int):
        query = db.query(SurveyAreas)
        total = query.count()
        data = query.offset(skip).limit(limit).all()
        return data, total

    @staticmethod
    def update(db: Session, area: SurveyAreas, data: dict):
        for key, value in data.items():
            setattr(area, key, value)
        db.commit()
        db.refresh(area)
        return area
