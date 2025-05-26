from src.data.models.tarea_base import TareaBase
from src.data.models.tarea_normal import TareaNormal
from src.data.models.tarea_urgente import TareaUrgente

class TareaGenerator:
    @staticmethod
    def crear_tarea(tipo: str, id:int, titulo:str, estado:bool, **kwargs) -> TareaBase:
        if tipo.lower() == 'normal':
            return TareaNormal(id, titulo, estado)
        if tipo.lower() == 'urgente':
            return TareaUrgente(id, titulo, estado, kwargs.get('fecha_limite',''))
        else:
            return TareaNormal(id, titulo, estado)
        