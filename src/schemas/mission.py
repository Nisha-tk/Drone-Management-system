from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel, Field
from typing import Optional
from src.enums.mission_status import MissionStatus

class MissionCreate(BaseModel):
    drone_id: UUID
    survey_area_id: UUID
    altitude: float
    overlap_percentage: float | None = None
    sensor_type: str | None = None
    data_collection_frequency: float | None = None


class MissionResponse(BaseModel):
    id: UUID
    drone_id: UUID
    operator_id: UUID
    survey_area_id: UUID
    status: MissionStatus
    progress_percent: float

    class Config:
        from_attributes = True





class MissionUpdate(BaseModel):
    altitude: Optional[float] = Field(gt=0)
    overlap_percentage: Optional[float] = Field(ge=0, le=100)
    sensor_type: Optional[str]
    data_collection_frequency: Optional[float] = Field(gt=0)
    status: Optional[MissionStatus]


