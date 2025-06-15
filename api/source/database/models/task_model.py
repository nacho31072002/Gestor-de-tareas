from datetime import date
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date

from .base_model import BaseModel


class TaskModel (BaseModel):
    __tablename__ = 'tasks'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo_tarea: Mapped[str] = mapped_column(String(10), nullable=False)
    estado: Mapped[str] = mapped_column(String(10), nullable=False)
    fecha_limite: Mapped[Optional[date]] = mapped_column(Date(), nullable=True)