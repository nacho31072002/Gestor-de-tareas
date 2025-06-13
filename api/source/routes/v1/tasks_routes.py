from typing import Annotated, Optional

from fastapi import APIRouter, Path, Query

from api.source.schemas.tasks_schemas import NewTasksRequest, UpdateTasksRequest, TaskResponse, TaskPaginatedResponse, TipoTarea
from .dependencies import task_controller

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
    tipo_tarea: Optional[TipoTarea] = Query(None)
) -> TaskPaginatedResponse:
    return await task_controller.get_paginated(page, limit, tipo_tarea)


@router.get(
    '/all',
    name='Lista todas las tareas',
    description='Lista todas las tareas sin paginar',
    response_description='Retorna una lista con todas las tareas.',
    status_code=200,
    responses={
        200: {'description': 'Lista de todas las tareas obtenida exitosamente.'},
        500: {'description': 'Error interno del servidor al obtener todas las tareas.'}
    }
)
async def get_all() -> list[TaskResponse]:
    return await task_controller.get_all()


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
    return await task_controller.create(new_task)
    

@router.get(
    '/{tasks_id}',
    name='Obtener tarea por ID',
    responses={
        200: {'description':'Tarea encontrada'},
        404: {'description':'Tarea no encontrada'}
    }
)
async def get_by_id(tasks_id: Annotated[int, Path(ge=1, description='Id de la tarea a buscar', title='Id de la tarea')]) -> TaskResponse:
    return await task_controller.get_by_id(tasks_id)

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
) -> TaskResponse:
    return await task_controller.update(tasks_id, task_data)


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
    return await task_controller.delete(tasks_id)