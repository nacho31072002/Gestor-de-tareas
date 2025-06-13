from fastapi import APIRouter


from .tasks_routes import router as tasks_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(tasks_router, tags=['Tasks'])
