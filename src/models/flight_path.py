from sqlalchemy import Column,  Enum , Integer , ForeignKey , DateTime , JSON , UUID
from src.db.base import Base 
from sqlalchemy.orm import relationship
from src.enums.flight_path import PathPattern


class FlightPaths(Base):
    mission_id = Column(UUID, ForeignKey("missions.id"), unique=True, nullable=False)
    pattern_type = Column(Enum(PathPattern), nullable=False)
    waypoints = Column(JSON, nullable=False) 

    mission = relationship("Missions", back_populates="flight_path")