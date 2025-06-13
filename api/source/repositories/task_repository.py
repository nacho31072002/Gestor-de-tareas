from typing import Dict, List, Any, Optional

from .base_repository import BaseRepository
from api.source.helpers.file_helpers import read_json_file, write_json_file
from api.source.config import app_settings
from api.source.schemas.tasks_schemas import TipoTarea


class TaskRepository(BaseRepository):
    async def _read_all(self) -> List[Dict[str, Any]]:
        data = read_json_file(app_settings.PATH_DATA)
        return data.get('tasks', [])

    async def _update_db(self, db: List[Dict[str, Any]]) -> None:
        current = read_json_file(app_settings.PATH_DATA)   
        current['tasks'] = db
        write_json_file(app_settings.PATH_DATA, current)

    async def _get_next_id(self) -> int:
        data = await self._read_all()
        if not data:
            return 1
        return max(tasks['id'] for tasks in data) + 1
    
    async def count(self, tipo_tarea: Optional[TipoTarea] = None) -> int:
        all_tasks = await self._read_all()
        if tipo_tarea:
            all_tasks = [t for t in all_tasks if t.get('tipo_tarea') == tipo_tarea.value]
        return len(all_tasks)

    async def get_list(self, page: int, limit: int, tipo_tarea: Optional[TipoTarea] = None) -> List[Dict[str, Any]]:
        all_tasks = await self._read_all()
        if tipo_tarea:
            all_tasks = [t for t in all_tasks if t.get('tipo_tarea') == tipo_tarea.value]
        start = (page - 1) * limit
        end = start + limit
        return all_tasks[start:end]
    
    async def get_all(self) -> List[Dict[str, Any]]:
        return await self._read_all()

    