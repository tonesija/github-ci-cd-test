from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "CI CD Test"
    DEBUG_MODE: bool = False

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class Settings(CommonSettings, ServerSettings):
    pass

settings = Settings()