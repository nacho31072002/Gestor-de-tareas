from .tarea_base import TareaBase
from typing import Dict
from datetime import datetime

class TareaUrgente(TareaBase):
    def __init__(self, id:int, titulo:str, estado:bool, fecha_limite:str = ''):
        super().__init__(id, titulo, estado)
        self.fecha_limite = fecha_limite
    
    def mostrar_info(self) -> str:
        limite_info = "⚠️  URGENTE"
        if self.fecha_limite:
            try:
                fecha_dt = datetime.fromisoformat(self.fecha_limite)
                fecha_str = fecha_dt.strftime("%d/%m/%Y") 
                limite_info = f"⚠️  Límite: {fecha_str}"
            except ValueError:
                limite_info = f"⚠️  Límite: {self.fecha_limite}" 

        return f"🚨 {self.titulo} - ({self.estado}) {limite_info}"
    
    def get_tipo(self) -> str:
        return "Urgente"
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data['fecha_limite'] = self.fecha_limite
        return data
    
    @classmethod
    def from_dict(cls, data:Dict):
        tarea = cls(data['id'], data['titulo'], data['estado'], data.get('fecha_creacion', ''))
        if 'fecha_creacion' in data:
            tarea.fecha_creacion = datetime.fromisoformat(data['fecha_creacion'])
        return tarea