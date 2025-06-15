from typing import Optional, List
from datetime import datetime, date

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from .paginated_schemas import PaginationMeta
from .enums import TipoTarea, EstadoTarea


class NewTasksRequest (BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    tipo_tarea: TipoTarea
    estado: EstadoTarea
    fecha_limite: Optional[date] = None


class UpdateTasksRequest (Partial[NewTasksRequest]):
    pass


class TaskResponse(BaseModel):
    id: int
    name: str
    tipo_tarea: TipoTarea
    estado: EstadoTarea
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    fecha_limite: Optional[date] = None


class TaskPaginatedResponse(BaseModel):
    result: List [TaskResponse]
    meta: PaginationMeta