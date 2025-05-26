from typing import List

from .db import initialize_data
from .models.tarea_base import TareaBase
from src.data.models.tarea_base import TareaBase
from src.data.models.tarea_normal import TareaNormal
from src.data.models.tarea_urgente import TareaUrgente

__all__ = [
    'TareaBase',
    'TareaNormal',
    'TareaUrgente'
    ]


tareas_db: List[TareaBase] = initialize_data()