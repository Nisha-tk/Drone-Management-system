
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from uuid import UUID
from src.enums.path_pattern import PathPattern


class Waypoint(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    altitude: float = Field(gt=0)




class FlightPathCreate(BaseModel):
    mission_id: UUID
    pattern_type: PathPattern
    waypoints: List[Waypoint] = Field(
        min_length=2,
        description="Ordered list of waypoints for the mission flight path",
    )




class FlightPathResponse(BaseModel):
    id: UUID
    mission_id: UUID
    pattern_type: PathPattern
    waypoints: List[Waypoint]

    class Config:
        from_attributes = True
