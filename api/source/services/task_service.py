import asyncio
from typing import List

from source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse
from source.exceptions import app_exceptions as ae


class TaskService():
    def __init__(self, task_repo):
        self.task_repo = task_repo

    async def get_paginated(self, page: int, limit: int) -> TaskPaginatedResponse:
        tasks, total_count = await asyncio.gather(
            self.__get__task_list(page, limit),
            self.__count()
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')

        return TaskPaginatedResponse(
            result=tasks,
            meta={
                'current_page': page,
                'total_pages': total_pages,
                'total_items': total_count,
                'items_per_page': limit,
                'has_next_page': page < total_pages,
                'has_previous_page': page > 1 
            }
        )
    
    async def create(self, data: NewTasksRequest) -> TaskResponse:
        from datetime import datetime
        return TaskResponse(
            id = 1,
            name = data.name,
            tipo_tarea = data.tipo_tarea,
            estado = False,
            created = datetime.now()
        )
    
    async def get_by_id(self, task_id: int) -> TaskResponse:
        raise ae.NotFoundError(f'La tarea #{task_id} no existe')

    async def update(self, task_id: int, data: UpdateTasksRequest) -> TaskResponse:
        raise ae.NotFoundError(f'La tarea #{task_id} no existe')

    async def delete(self, task_id: int) -> None:
        raise ae.NotFoundError(f'La tarea #{task_id} no existe')
    
    async def __count(self) -> int:
        return 0

    async def __get__task_list(self, page: int, limit: int) -> List[TaskResponse]:
        return []
