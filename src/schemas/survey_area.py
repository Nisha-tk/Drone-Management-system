from pydantic import BaseModel, Field
from typing import List, Dict
from uuid import UUID

class SurveyAreaCreate(BaseModel):
    name: str = Field(min_length=2)
    polygon_coordinates: List[Dict[str, float]]
    total_area_sq_m: float | None = None


class SurveyAreaResponse(BaseModel):
    id: UUID
    name: str
    polygon_coordinates: list
    total_area_sq_m: float | None

    class Config:
        from_attributes = True



from typing import Optional

class SurveyAreaUpdate(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=100)
    polygon_coordinates: Optional[list]
    total_area_sq_m: Optional[float] = Field(gt=0)

