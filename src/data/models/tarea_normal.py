from .tarea_base import TareaBase
from typing import Dict
from datetime import datetime

class TareaNormal(TareaBase):
    def __init__(self, id:int, titulo:str, estado:bool):
        super().__init__(id, titulo, estado)

    def mostrar_info(self) -> str:
        return f"📝 {self.titulo} ({self.estado})"
    
    def get_tipo(self) -> str:
        return "Normal"
    
    @classmethod
    def from_dict(cls, data:Dict):
        tarea = cls(data['id'], data['titulo'], data['estado'])
        if 'fecha_creacion' in data:
            tarea.fecha_creacion = datetime.fromisoformat(data['fecha_creacion'])
        return tarea