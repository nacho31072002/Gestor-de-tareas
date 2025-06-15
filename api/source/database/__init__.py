from .database_connection import DatabaseConnection
from api.source.config import app_settings
from .models import BaseModel


db_conection = DatabaseConnection(app_settings.DB_CONN)

def create_tables():
    BaseModel.metadata.create_all(bind=db_conection.engine)