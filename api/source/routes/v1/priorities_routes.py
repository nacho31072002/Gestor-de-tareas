from fastapi import APIRouter, Path, Query

from typing import Annotated
from datetime import datetime

from source.schemas.priorities_schemas import PriorityResponse, PriorityPaginatedResponse, NewPriorityRequest, UpdatePriorityRequest  
from .dependencies import priority_controller

router = APIRouter(
    prefix='/priorities',
    responses={
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros.'},
        401: {'description': 'Unauthorized. Credenciales inválidas o no enviadas.'},
        403: {'description': 'Forbidden. No tienes acceso a este recurso.'},
        500: {'description': 'Internal Server Error. Error del servidor no manejado, contacta al sysadmin.'},
        501: {'description': 'Not Implemented. Esta función no está implementada aún, pero lo estará en futuras versiones.'},
    }
)

@router.get(
    '',
    name='Lista paginada de prioridades',
    description='Lista de prioridades paginadas',
    response_description='Retorna una lista de prioridades y datos de paginación.',
    status_code=200,
    responses={
        400: {'description': 'Bad request. Revisa los parámetros de paginación o filtrado.'}
    }
)
async def get_paginated_priorities(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
) -> PriorityPaginatedResponse:
    return await priority_controller.get_paginated(page, limit)

@router.post(
    '',
    name='Crear nueva prioridad',
    status_code=201,
    responses={
        201: {'description': 'Nueva prioridad creada exitosamente'},
        400: {'description': 'Revisa el body request'},
    }
)
async def create_priority(new_priority: NewPriorityRequest) -> PriorityResponse:
    return await priority_controller.create(new_priority)

@router.get(
    '/{priority_id}',
    name='Obtener prioridad por ID',
    responses={
        200: {'description': 'Prioridad encontrada'},
        404: {'description': 'Prioridad no encontrada'}
    }
)
async def get_priority_by_id(
    priority_id: Annotated[int, Path(ge=1, description='ID de la prioridad', title='ID')]
) -> PriorityResponse:
    return await priority_controller.get_by_id(priority_id)

@router.patch(
    '/{priority_id}',
    name='Actualizar prioridad por ID',
    response_model=PriorityResponse,
    responses={
        200: {'description': 'Prioridad actualizada'},
        404: {'description': 'Prioridad no encontrada'}
    }
)
async def update_priority_by_id(
    priority_id: Annotated[int, Path(ge=1, title='ID de la prioridad')],
    priority_data: UpdatePriorityRequest
) -> PriorityResponse:
    return await priority_controller.update(priority_id, priority_data)

@router.delete(
    '/{priority_id}',
    name='Borrar prioridad por ID',
    status_code=204,
    responses={
        204: {'description': 'Prioridad borrada'},
        404: {'description': 'Prioridad no encontrada'}
    }
)
async def delete_priority_by_id(priority_id: Annotated[int, Path(ge=1, title='ID de la prioridad')]):
    return await priority_controller.delete(priority_id)
