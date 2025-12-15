from sqlalchemy import Column, String , Float , Enum
from src.db.base import Base 
from sqlalchemy.orm import relationship
from src.enums.drones_status import DroneStatus




class Drones(Base):
    name = Column(String, nullable=False)
    model = Column(String, nullable=True)
    
    status = Column(Enum(DroneStatus), default=DroneStatus.AVAILABLE)
    battery_level = Column(Float, default=100.0)

    last_known_lat = Column(Float, nullable=True)
    last_known_lng = Column(Float, nullable=True)

    
    missions = relationship("Missions", back_populates="drone")
