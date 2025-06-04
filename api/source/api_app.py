from fastapi import FastAPI

from .routes import api_router

api_server = FastAPI(
    description='Proyecto Tareas + FastApi',
    version='0.0.0',
    title='FastApi'                 
    )


api_server.include_router(api_router)