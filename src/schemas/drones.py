from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from src.enums.drones_status import DroneStatus


class DroneCreate(BaseModel):
    name: str = Field(min_length=2)
    model: str = Field(min_length=1)
    
                # in km


class DroneResponse(BaseModel):
    id: UUID
    name: str
    model: str
    

    class Config:
        from_attributes = True



class DroneUpdate(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=50)
    model: Optional[str] = Field(min_length=2, max_length=50)
    status: Optional[DroneStatus]
    battery_level: Optional[float] = Field(ge=0, le=100)
    last_known_lat: Optional[float]
    last_known_lng: Optional[float]

