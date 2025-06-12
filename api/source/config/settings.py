from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 8000
    DEV: bool =  True

    class Config:
        env_file = '.env'    