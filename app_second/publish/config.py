from pydantic_settings import BaseSettings, SettingsConfigDict
from aiologger import Logger

logger = Logger.with_default_handlers(name="publish_logger")

class Config(BaseSettings):
    URL_BROKER: str
    QUEUE_NAME: str
    APP_NAME: str = "test_2_publisher"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )
    
setting = Config()