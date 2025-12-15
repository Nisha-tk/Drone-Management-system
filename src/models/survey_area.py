from sqlalchemy import Column, String , Float , JSON
from src.db.base import Base 
from sqlalchemy.orm import relationship

class SurveyAreas(Base):
    name = Column(String, nullable=False)
    polygon_coordinates = Column(JSON, nullable=False)  
    total_area_sq_m = Column(Float, nullable=True)

    missions = relationship("Missions", back_populates="survey_area")