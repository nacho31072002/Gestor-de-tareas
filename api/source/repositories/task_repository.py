from typing import Dict, List, Any

from .base_repository import BaseRepository
from api.source.helpers.file_helpers import read_json_file, write_json_file
from api.source.config import app_settings


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
    
    