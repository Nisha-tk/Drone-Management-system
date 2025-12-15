from sqlalchemy import Column, String , Float , Enum , Integer , ForeignKey , DateTime , UUID
from src.db.base import Base 
from sqlalchemy.orm import relationship
from src.enums.mission_status import MissionStatus


class Missions(Base):
    drone_id = Column(UUID(as_uuid=True), ForeignKey("drones.id"), nullable=False)
    operator_id = Column(UUID(as_uuid= True), ForeignKey("users.id"), nullable=False)
    survey_area_id = Column(UUID(as_uuid=True), ForeignKey("surveyareas.id"), nullable=False)

    altitude = Column(Float, nullable=False)
    overlap_percentage = Column(Float, nullable=True)
    sensor_type = Column(String, nullable=True)
    data_collection_frequency = Column(Float, nullable=True)

    status = Column(Enum(MissionStatus), default=MissionStatus.PLANNED)
    progress_percent = Column(Float, default=0.0)

    start_time = Column(DateTime(timezone=True), nullable=True)
    end_time = Column(DateTime(timezone=True), nullable=True)

   
    drone = relationship("Drones", back_populates="missions")
    operator = relationship("Users", back_populates="missions")
    survey_area = relationship("SurveyAreas", back_populates="missions")

    flight_path = relationship("FlightPaths", back_populates="mission", uselist=False)
    report = relationship("MissionReports", back_populates="mission", uselist=False)
