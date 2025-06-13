from typing import Optional

import logging

from api.source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse, TipoTarea
from api.source.exceptions.server_exceptions import InternalServerError
from api.source.exceptions.client_exceptions import NotFound
from api.source.exceptions import app_exceptions as ae
from api.source.services.task_service import TaskService


logger = logging.getLogger(__name__)

class TaskController():
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    async def get_paginated(self, page: int, limit: int, tipo_tarea: Optional[TipoTarea] = None) -> TaskPaginatedResponse:
        try:
            return await self.task_service.get_paginated(page, limit, tipo_tarea)
        except ae.NotFoundError as ex:
            logger.error(f'Pagina {page} no existe. Items por pagina: {limit}')
            raise NotFound(ex.message, 'TASK_PAGE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al listar tareas: {ex}')
            raise InternalServerError(
                message=f'Error al listar tareas',
                exception_code='TASK_UNHANDLED_ERROR'
            )
    
    async def get_all(self) -> list[TaskResponse]:
        try:
            return await self.task_service.get_all()
        except Exception as ex:
            logger.critical(f'Error desconocido al listar todas las tareas: {ex}')
            raise InternalServerError(
                message='Error al listar todas las tareas',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def create(self, data: NewTasksRequest) -> TaskResponse:
        try:
            return await self.task_service.create(data)
        except Exception as ex:
            logger.critical(f'Error desconocido al crear la tarea: {ex}')
            raise InternalServerError(
                message=f'Error al crear la tarea "{data.name}"',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def get_by_id(self, task_id: int) -> TaskResponse:
        try:
            return await self.task_service.get_by_id(task_id)
        except ae.NotFoundError as ex:
            logger.error(f'La tarea #{task_id} no encontrada')
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al obtener la tarea #{task_id}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener la tarea "{task_id}"',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def update(self, task_id: int, data: UpdateTasksRequest) -> TaskResponse:
        try:
            return await self.task_service.update(task_id, data)
        except ae.NotFoundError as ex:
            logger.error(f'La tarea #{task_id} no encontrada')
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al actualizar la tarea #{task_id}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar la tarea #{task_id}',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def delete(self, task_id: int) -> None:
        try:
            return await self.task_service.delete(task_id)
        except ae.NotFoundError as ex:
            logger.error(f'La tarea #{task_id} no encontrada')
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al eliminar la tarea #{task_id}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar la tarea #{task_id}',
                exception_code='TASK_UNHANDLED_ERROR'
            )