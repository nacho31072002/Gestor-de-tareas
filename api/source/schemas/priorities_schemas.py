from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from typing import Optional, List
from datetime import datetime

from api.source.schemas.paginated_schemas import PaginationMeta

class NewPriorityRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)


class UpdatePriorityRequest(Partial[NewPriorityRequest]):
    pass


class PriorityResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created: Optional[datetime] = None


class PriorityPaginatedResponse(BaseModel):
    result: List[PriorityResponse]
    meta: PaginationMeta
