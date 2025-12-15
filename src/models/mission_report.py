from sqlalchemy import Column,  String,   ForeignKey , Float , UUID
from src.db.base import Base 
from sqlalchemy.orm import relationship

class MissionReports(Base):
    mission_id = Column(UUID(as_uuid=True), ForeignKey("missions.id"), unique=True, nullable=False)

    total_flight_time = Column(Float, nullable=True)      
    total_distance = Column(Float, nullable=True)         
    total_coverage = Column(Float, nullable=True)         
    battery_used = Column(Float, nullable=True)
    summary_notes = Column(String, nullable=True)

    mission = relationship("Missions", back_populates="report")