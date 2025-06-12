import asyncio
from typing import List

from api.source.schemas.priorities_schemas import PriorityPaginatedResponse, UpdatePriorityRequest, PriorityResponse, NewPriorityRequest 
from api.source.exceptions import app_exceptions as ae


class PriorityService():
    def __init__(self, priority_repo):
        self.priority_repo = priority_repo

    async def get_paginated(self, page: int, limit: int) -> PriorityPaginatedResponse:
        priorities, total_count = await asyncio.gather(
            self.__get__priority_list(page, limit),
            self.__count()
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')

        return PriorityPaginatedResponse(
            result=priorities,
            meta={
                'current_page': page,
                'total_pages': total_pages,
                'total_items': total_count,
                'items_per_page': limit,
                'has_next_page': page < total_pages,
                'has_previous_page': page > 1 
            }
        )
    
    async def create(self, data: NewPriorityRequest) -> PriorityResponse:
        from datetime import datetime
        return PriorityResponse(
            id= 1,
            name= data.name,
            description= data.description,
            created= datetime.now()
        )
    
    async def get_by_id(self, priority_id: int) -> PriorityResponse:
        raise ae.NotFoundError(f'La prioridad #{priority_id} no existe')

    async def update(self, priority_id: int, data: UpdatePriorityRequest) -> PriorityResponse:
        raise ae.NotFoundError(f'La prioridad #{priority_id} no existe')

    async def delete(self, priority_id: int) -> None:
        raise ae.NotFoundError(f'La prioridad #{priority_id} no existe')
    
    async def __count(self) -> int:
        return 0

    async def __get__priority_list(self, page: int, limit: int) -> List[PriorityResponse]:
        return []