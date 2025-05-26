from .tarea_normal import TareaNormal
from .tarea_base import TareaBase
from .tarea_urgente import TareaUrgente

TIPO_MAP = {
    "Normal": TareaNormal,
    "Urgente": TareaUrgente
}

def tarea_from_dict(data: dict) -> TareaBase:
    tipo = data.get("tipo")
    cls = TIPO_MAP.get(tipo)
    if cls is None:
        raise ValueError(f"Tipo de tarea desconocido: {tipo}")
    return cls.from_dict(data)
