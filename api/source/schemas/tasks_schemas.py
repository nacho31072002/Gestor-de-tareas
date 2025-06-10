from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field

from .paginated_schemas import PaginationMeta


class NewTasksRequest (BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    tipo_tarea: str
    estado: bool
    posicion: Optional[int] = None


class UpdateTasksRequest (BaseModel):
    id: Optional[int]
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    tipo_tarea: Optional[str]
    estado: Optional[bool]
    posicion: Optional[int] = None


class TaskResponse(BaseModel):
    id: int
    name: str
    tipo_tarea: str
    estado: bool
    created: Optional[datetime] = None


class TaskPaginatedResponse(BaseModel):
    result: List [TaskResponse]
    meta: PaginationMeta