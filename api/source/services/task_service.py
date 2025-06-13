import logging
from typing import List

from api.source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse
from api.source.exceptions import app_exceptions as ae
from api.source.repositories.task_repository import TaskRepository

logger = logging.getLogger(__name__)

class TaskService():
    def __init__(self, task_repo: TaskRepository = TaskRepository()):
        if task_repo is None:
            task_repo = TaskRepository()
        self.task_repo = task_repo

    async def get_paginated(self, page: int, limit: int) -> TaskPaginatedResponse:
        logger.debug(f'Obteniendo tareas paginadas. Pagina: {page}, Limite: {limit}')
        
        total_count = await self.task_repo.count()
        tasks_data = await self.task_repo.get_list(page, limit)

        tasks = [
            TaskResponse(
                id=task['id'],
                name=task['name'],
                tipo_tarea=task['tipo_tarea'],
                estado=task['estado'],
                created=task.get('created_at', task.get('created'))
            )
            for task in tasks_data
        ]

        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')
            
        logger.debug(f'Tareas obtenidas: {len(tasks)}')
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
        logger.debug(f'Creando tarea: {data}')
        new_task = await self.task_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Tarea creada: {new_task}')
        return TaskResponse.model_validate(new_task)

    async def get_by_id(self, task_id: int) -> TaskResponse:
        logger.debug(f'Obteniendo tarea por ID: {task_id}')
        task = await self.task_repo.get_one_by_criteria({'id': task_id})
        if task is None:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')
        return TaskResponse.model_validate(task)
    
    async def update(self, task_id: int, data: UpdateTasksRequest) -> TaskResponse:
        logger.debug(f'Actualizando tarea #{task_id} con datos: {data}')
        task = await self.task_repo.update_one({'id': task_id}, data.model_dump(mode='json', exclude_unset=True))
        if task is None:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')
        return TaskResponse.model_validate(task)

    async def delete(self, task_id: int) -> None:
        logger.debug(f'Eliminando tarea #{task_id}')
        delete = await self.task_repo.delete_one({'id': task_id})
        if not delete:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')
        return None
    
    async def __count(self) -> int:
        return await self.task_repo.count()

    async def __get__task_list(self, page: int, limit: int) -> List[TaskResponse]:
        return await self.task_repo.get_list(page, limit)
