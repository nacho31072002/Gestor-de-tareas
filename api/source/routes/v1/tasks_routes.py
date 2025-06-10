import sys
import os
from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Path, Query

from source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse

router = APIRouter(
    prefix='/tasks',
    responses={
        400: {'description':'Bad Request. Revisa la info del body y/o parametros.'},
        401: {'description':'Unauthorized. Credenciales invalidas o no enviadas.'},
        403: {'description':'Forbidden. No tienes acceso a este recurso.'},
        500: {'description':'Internal Server Error. Error del servidor no manejado, contacta al sysadmin. '},
        501: {'description':'Not Implemented. Esta funcion no esta implementada aun, pero lo estara en futuras versiones.'},
    }
)

@router.get(
    '',
    name='Lista paginada',
    description='Lista de tareas paginadas',
    response_description='Retorna un objeto con la lista de resultado y la info de la paginacion.',
    status_code=200,
    responses={
        400: {'description':'Bad request. Revisa los parametros de paginacion o filtrado.'}
    }
)
async def get_paginated(
    page:Annotated[int, Query(ge=1)] = 1, 
    limit:Annotated[int, Query(ge=1, le=100)] = 10,
) -> TaskPaginatedResponse:
    return {
       'result': [
           {
            'id' : 1,
            'name' : 'estudiar',
            'tipo_tarea' : 'normal',
            'estado' : False,
            'created' : datetime.now()
           }
        ],
       'meta': {
           'current_page': page,
           'total_pages': 1,
           'total_items': 0,
           'items_per_page': limit,
           'has_next_page': False,
           'has_previous_page': False,
       }
    }


@router.post(
    '',
    name='Crear nueva tarea',
    status_code=201,
    responses={
        201: {'description':'Nuevo tarea creada exitosamente'},
        400: {'description':'Revisa el body request'},
    }
)
async def create(new_task: NewTasksRequest) -> TaskResponse:
    return TaskResponse(
        id = 1,
        name = 'Entrega TP',
        tipo_tarea = 'normal',
        estado = False,
        created = datetime.now()
    )
    

@router.get(
    '/{tasks_id}',
    name='Obtener tarea por ID',
    responses={
        200: {'description':'Tarea encontrada'},
        404: {'description':'Tarea no encontrada'}
    }
)
async def get_by_id(
    tasks_id: Annotated[int, Path(ge=1, 
    description='Id de la tarea a buscar', 
    title='Id de la tarea')]
) -> TaskResponse:
    return TaskResponse (
        id = tasks_id,
        name = 'estudiar',
        tipo_tarea = 'normal',
        estado = False,
        created = datetime.now()
    )


@router.patch(
    '/{tasks_id}',
    name='Actualizar datos de tareas por ID.',
    response_model = TaskResponse,
    responses={
        200: {'description':'Tarea actualizada'},
        404: {'description':'Tarea para actualizar no encontrada'}
    }
)
async def update_by_id(
    tasks_id: Annotated[int, Path(ge=1, title='Id de la tarea')], 
    task_data: UpdateTasksRequest
):
    return {
        'id' : tasks_id,
        'name' : 'estudiar',
        'tipo_tarea' : 'normal',
        'estado' : False,
        'created' : datetime.now()
    }


@router.delete(
    '/{tasks_id}',
    name='Borrar tarea por ID',
    status_code=204,
    responses={
        204: {'description':'Tarea borrada.'},
        404: {'description':'Tarea para borrar no encontrada.'}
    }

)
async def delete_by_id(tasks_id: Annotated[int, Path(ge=1, title='Id de la tarea')]):
    return None