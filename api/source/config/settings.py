from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 8000
    DEV: bool =  True

    LOG_DIR: str = 'logs'
    DEBUG: bool = False

    PATH_DATA: str = 'database/fake_db.json'

    class Config:
        env_file = '.env'    