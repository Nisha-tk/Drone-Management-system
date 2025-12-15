from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class MissionReportCreate(BaseModel):
    mission_id: UUID

    summary: str = Field(
        min_length=10,
        max_length=1000,
        description="High-level mission summary"
    )

    total_flight_time: float = Field(
        gt=0,
        description="Total flight time in minutes"
    )

    area_covered_sq_m: float = Field(
        gt=0,
        description="Total area covered in square meters"
    )


class MissionReportResponse(BaseModel):
    id: UUID
    mission_id: UUID

    summary: str
    total_flight_time: float
    area_covered_sq_m: float

    created_at: datetime

    class Config:
        from_attributes = True
