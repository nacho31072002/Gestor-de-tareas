import logging
from typing import List, Optional
from datetime import datetime, date

from api.source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse
from api.source.schemas.enums import TipoTarea, EstadoTarea
from api.source.exceptions import app_exceptions as ae
from api.source.exceptions import server_exceptions as se
from api.source.repositories.task_repository import TaskRepository

logger = logging.getLogger(__name__)

class TaskService():
    def __init__(self, task_repo: TaskRepository = TaskRepository()):
        if task_repo is None:
            task_repo = TaskRepository()
        self.task_repo = task_repo

    async def get_paginated(self, page: int, limit: int, tipo_tarea: Optional[TipoTarea] = None) -> TaskPaginatedResponse:
        logger.debug(f'Obteniendo tareas paginadas. Pagina: {page}, Limite: {limit}, Filtro tipo_tarea: {tipo_tarea}')

        total_count = await self.task_repo.count(tipo_tarea)
        tasks_data = await self.task_repo.get_list(page, limit, tipo_tarea)

        tasks = [
            TaskResponse(
                id=task['id'],
                name=task['name'],
                tipo_tarea=TipoTarea(task['tipo_tarea']),
                estado=EstadoTarea(task['estado']),
                fecha_creacion=datetime.fromisoformat(task.get('created_at', task.get('created'))),
                fecha_actualizacion = datetime.fromisoformat(task['updated_at']) if task.get('updated_at') else None,
                fecha_limite=date.fromisoformat(task['fecha_limite']) if task.get('fecha_limite') else None
            )
            for task in tasks_data
        ]

        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Página {page} no existe')

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

    async def get_all(self) -> List[TaskResponse]:
        logger.debug('Obteniendo todas las tareas')
        tasks_data = await self.task_repo.get_all()
        tasks = [
            TaskResponse(
                id=task['id'],
                name=task['name'],
                tipo_tarea=TipoTarea(task['tipo_tarea']),
                estado=EstadoTarea(task['estado']),
                fecha_creacion=datetime.fromisoformat(task['created_at']),
                fecha_actualizacion = datetime.fromisoformat(task['updated_at']) if task.get('updated_at') else None,
                fecha_limite=date.fromisoformat(task['fecha_limite']) if task.get('fecha_limite') else None
            )
            for task in tasks_data
        ]
        logger.debug(f'Tareas obtenidas: {len(tasks)}')
        return tasks
    

    async def create(self, data: NewTasksRequest) -> TaskResponse:
        if data.tipo_tarea == TipoTarea.URGENTE and not data.fecha_limite:
            raise se.BadRequestError("Las tareas URGENTES deben tener una fecha límite.")

        logger.debug(f'Creando tarea: {data}')

        now = datetime.now()

        task_dict = data.model_dump(mode='json')
        task_dict['created_at'] = now.isoformat()
        task_dict['updated_at'] = now.isoformat()

        new_task = await self.task_repo.create(task_dict)
        logger.debug(f'Tarea creada: {new_task}')

        return TaskResponse(
            id=new_task['id'],
            name=new_task['name'],
            tipo_tarea=TipoTarea(new_task['tipo_tarea']),
            estado=EstadoTarea(new_task['estado']),
            fecha_creacion=datetime.fromisoformat(new_task['created_at']),
            fecha_actualizacion=datetime.fromisoformat(new_task['updated_at']),
            fecha_limite=date.fromisoformat(new_task['fecha_limite']) if new_task.get('fecha_limite') else None
        )


    async def get_by_id(self, task_id: int) -> TaskResponse:
        logger.debug(f'Obteniendo tarea por ID: {task_id}')
        task = await self.task_repo.get_one_by_criteria({'id': task_id})
        if task is None:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')
        
        return TaskResponse(
            id=task['id'],
            name=task['name'],
            tipo_tarea=TipoTarea(task['tipo_tarea']),
            estado=EstadoTarea(task['estado']),
            fecha_creacion=datetime.fromisoformat(task['created_at']),
            fecha_actualizacion = datetime.fromisoformat(task['updated_at']) if task.get('updated_at') else None,
            fecha_limite=date.fromisoformat(task['fecha_limite']) if task.get('fecha_limite') else None
        )


    async def update(self, task_id: int, data: UpdateTasksRequest) -> TaskResponse:
        logger.debug(f'Actualizando tarea #{task_id} con datos: {data}')
        task = await self.task_repo.update_one({'id': task_id}, data.model_dump(mode='json', exclude_unset=True))
        if task is None:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')

        return TaskResponse(
            id=task['id'],
            name=task['name'],
            tipo_tarea=TipoTarea(task['tipo_tarea']),
            estado=EstadoTarea(task['estado']),
            fecha_creacion=datetime.fromisoformat(task['created_at']),
            fecha_actualizacion = datetime.fromisoformat(task['updated_at']) if task.get('updated_at') else None,
            fecha_limite=date.fromisoformat(task['fecha_limite']) if task.get('fecha_limite') else None
        )

    async def delete(self, task_id: int) -> None:
        logger.debug(f'Eliminando tarea #{task_id}')
        delete = await self.task_repo.delete_one({'id': task_id})
        if not delete:
            raise ae.NotFoundError(f'La tarea #{task_id} no existe')
        return None