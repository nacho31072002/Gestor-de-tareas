from source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse
from source.exceptions.server_exceptions import InternalServerError, NotImplemented
from source.exceptions.client_exceptions import NotFound
from source.exceptions import app_exceptions as ae
from source.exceptions.base_hhtp_exception import BaseHTTPException
from source.services.task_service import TaskService


class TaskController():
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    async def get_paginated(self, page: int, limit: int) -> TaskPaginatedResponse:
        try:
            return await self.task_service.get_paginated(page, limit)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='TASK ENDPOINT NOT IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'TASK_PAGE_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar tareas',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def create(self, data: NewTasksRequest) -> TaskResponse:
        try:
            return await self.task_service.create(data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='TASK ENDPOINT NOT IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear la tarea "{data.name}"',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def get_by_id(self, task_id: int) -> TaskResponse:
        try:
            return await self.task_service.get_by_id(task_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='TASK ENDPOINT NOT IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener la tarea "{task_id}"',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def update(self, task_id: int, data: UpdateTasksRequest) -> TaskResponse:
        try:
            return await self.task_service.update(task_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='TASK ENDPOINT NOT IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar la tarea #{task_id}',
                exception_code='TASK_UNHANDLED_ERROR'
            )

    async def delete(self, task_id: int) -> None:
        try:
            return await self.task_service.delete(task_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='TASK ENDPOINT NOT IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'TASK_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar la tarea #{task_id}',
                exception_code='TASK_UNHANDLED_ERROR'
            )