from .base_model import DataModel


class TareaModel(DataModel):
    def __init__(self, id: int, titulo: str, estado: bool):
        self._id: int = id
        self._titulo: str = titulo
        self._estado: bool = estado

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id=int) -> None:
        self._id = id

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo=str) -> None:
        self._titulo = titulo

    @property
    def estado(self) -> bool:
        return self._estado
    
    @estado.setter
    def estado(self, estado=bool) -> None:
        self._estado = estado
    
    def to_jason(self) -> dict:
        return {
            "id" : self.id,
            "titulo" : self.titulo,
            "estado" : self.estado
        }
    
