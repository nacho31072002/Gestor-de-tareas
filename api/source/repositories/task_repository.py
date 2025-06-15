from typing import Dict, List, Any, Optional

from .base_repository import BaseRepository
from api.source.schemas.tasks_schemas import TipoTarea
from api.source.database.models import TaskModel


class TaskRepository(BaseRepository):
    
    def __init__(self):
        super().__init__(TaskModel)

    async def count(self, tipo_tarea: Optional[TipoTarea] = None) -> int:
        if tipo_tarea:
            criteria = {'tipo_tarea': tipo_tarea.value}
        else:
            criteria = {}
        return await super().count(criteria)

    async def get_list(self, page: int, limit: int, tipo_tarea: Optional[TipoTarea] = None) -> List[Dict[str, Any]]:
        if tipo_tarea:
            criteria = {'tipo_tarea': tipo_tarea.value}
        else:
            criteria = {}
        return await super().get_list(page, limit, criteria)
    
    async def get_all(self) -> List[Dict[str, Any]]:
        return await super().get_list(1, 10000, {})

    async def _read_all(self) -> List[Dict[str, Any]]:
        return []
    
    async def _update_db(self, db: List[Dict[str, Any]]) -> None:
        pass
    
    async def _get_next_id(self) -> int:
        return 0