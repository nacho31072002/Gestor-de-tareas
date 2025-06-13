import logging
from fastapi import FastAPI

from .routes import api_router
from .config.logger import configure_logging


configure_logging()

logger = logging.getLogger(__name__)

api_server = FastAPI(
    description='Proyecto Tareas + FastApi',
    version='0.0.0',
    title='FastApi'                 
    )


api_server.include_router(api_router)