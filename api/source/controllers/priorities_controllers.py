from source.schemas.priorities_schemas import NewPriorityRequest, UpdatePriorityRequest, PriorityResponse, PriorityPaginatedResponse
from source.exceptions.server_exceptions import InternalServerError, NotImplemented
from source.exceptions.client_exceptions import NotFound
from source.exceptions import app_exceptions as ae
from source.exceptions.base_hhtp_exception import BaseHTTPException
from source.services.priority_service import PriorityService


class PrioritiesController():
    def __init__(self, priorities_service: PriorityService):
        self.priorities_service = priorities_service

    async def get_paginated(self, page: int, limit: int) -> PriorityPaginatedResponse:
        try:
            return await self.priorities_service.get_paginated(page, limit)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='PRIORITY_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'PRIORITY_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al paginar prioridades',
                exception_code='PRIORITY_UNHANDLED_ERROR'
            )

    async def create(self, data: NewPriorityRequest) -> PriorityResponse:
        try:
            return await self.priorities_service.create(data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='PRIORITY_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear prioridad "{data.name}"',
                exception_code='PRIORITY_UNHANDLED_ERROR'
            )

    async def get_by_id(self, priority_id: int) -> PriorityResponse:
        try:
            return await self.priorities_service.get_by_id(priority_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='PRIORITY_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'PRIORITY_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener prioridad #{priority_id}',
                exception_code='PRIORITY_UNHANDLED_ERROR'
            )

    async def update(self, priority_id: int, data: UpdatePriorityRequest) -> PriorityResponse:
        try:
            return await self.priorities_service.update(priority_id, data)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='PRIORITY_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'PRIORITY_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar la prioridad #{priority_id}',
                exception_code='PRIORITY_UNHANDLED_ERROR'
            )

    async def delete(self, priority_id: int) -> None:
        try:
            return await self.priorities_service.delete(priority_id)
            #raise NotImplemented('Endpoint get paginated not implemented', exception_code='PRIORITY_ENDPOINT_NOT_IMPLEMENTED')
        except ae.NotFoundError as ex:
            raise NotFound(ex.message, 'PRIORITY_NOT_FOUND')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar la prioridad #{priority_id}',
                exception_code='PRIORITY_UNHANDLED_ERROR'
            )