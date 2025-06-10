from pydantic import BaseModel, Field

from typing import Optional, List
from datetime import datetime

from .paginated_schemas import PaginationMeta

class NewPriorityRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)


class UpdatePriorityRequest(BaseModel):
    id: Optional[int]
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)


class PriorityResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created: Optional[datetime] = None


class PriorityPaginatedResponse(BaseModel):
    result: List[PriorityResponse]
    meta: PaginationMeta
