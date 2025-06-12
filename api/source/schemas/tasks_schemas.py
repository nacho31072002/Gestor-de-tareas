from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from .paginated_schemas import PaginationMeta


class NewTasksRequest (BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    tipo_tarea: str
    estado: bool
    posicion: Optional[int] = None


class UpdateTasksRequest (Partial[NewTasksRequest]):
    pass


class TaskResponse(BaseModel):
    id: int
    name: str
    tipo_tarea: str
    estado: bool
    created: Optional[datetime] = None


class TaskPaginatedResponse(BaseModel):
    result: List [TaskResponse]
    meta: PaginationMeta