from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime, date
from typing import Type

from api.source.database import db_conection
from api.source.database.models import BaseModel


class BaseRepository(ABC):

    def __init__(self, Model: Type[BaseModel]):
        self.db = db_conection.session
        self.Model = Model

    async def count(self, criteria: dict = {}) -> int:
        count = self.db.query(self.Model).filter_by(**criteria).count()
        return count

    async def get_list(self, page: int, limit: int, criteria: dict = {}) -> list[dict]:
        offset = (page - 1) * limit
        records = self.db.query(self.Model).order_by('id').filter_by(**criteria).limit(limit).offset(offset).all()
        return [self._to_dict(record) for record in records]

    async def create(self, data: dict) -> dict:
        new_record = self.Model(**data)
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
        return self._to_dict(new_record)

    async def get_one_by_criteria(self, criteria: dict) -> dict | None:
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return None
        return self._to_dict(record)

    async def update_one(self, criteria: dict, data: dict) -> dict | None:
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return None
        for field in data.keys():
            setattr(record, field, data[field])
        self.db.commit()
        self.db.refresh(record)
        return self._to_dict(record)

    async def delete_one(self, criteria: dict) -> bool:
        record = self.db.query(self.Model).filter_by(**criteria).first()
        if record is None:
            return False
        self.db.delete(record)
        self.db.commit()
        return True

    @abstractmethod
    async def _read_all(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def _update_db(self, db: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    async def _get_next_id(self) -> int:
        pass

    def _to_dict(self, record: BaseModel) -> dict:
        result = {}
        for column in self.Model.__table__.columns:
            value = getattr(record, column.name)
            if isinstance(value, datetime):
                result[column.name] = value.isoformat()
            elif isinstance(value, date):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
                
        return result