from enum import Enum


class TipoTarea(str, Enum):
    NORMAL = 'normal'
    URGENTE = 'urgente'


class EstadoTarea(str, Enum):
    PENDIENTE = 'pendiente'
    COMPLETADA = 'completada'