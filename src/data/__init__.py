from typing import List

from .db import initialize_data
from .models.tarea_model import TareaModel

tareas_db: List[TareaModel] = initialize_data()