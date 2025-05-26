from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict


class TareaBase(ABC):
    def __init__(self, id: int, titulo: str, estado: bool):
        self.id: int = id
        self.titulo: str = titulo
        self.estado: bool = estado
        self.fecha_creacion = datetime.now()

    @abstractmethod
    def mostrar_info(self) -> str:
        pass

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    def cambiar_estado(self, nuevo_estado: bool):
        self.estado = nuevo_estado
    
    def to_dict(self) -> Dict:
        return {
            "id" : self.id,
            "titulo" : self.titulo,
            "estado" : self.estado,
            "tipo" : self.get_tipo(),
            "fecha_creacion" : self.fecha_creacion.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        pass
    
