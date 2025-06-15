from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routes import api_router
from .config.logger import configure_logging
from .database import db_conection, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Antes de levantar el servidor
    configure_logging()
    if db_conection.connect():
        create_tables()
    yield
    db_conection.disconnect()
    # Antes de cerrar el servidor
   
api_server = FastAPI(
    description='Proyecto Tareas + FastApi',
    version='0.0.0',
    title='FastApi',
    lifespan=lifespan                
)


api_server.include_router(api_router)