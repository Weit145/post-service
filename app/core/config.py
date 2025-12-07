import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    db_url: str = os.getenv("DB_URL", "sqlite+aiosqlite:///:memory:")
    db_echo: bool = False

    kafka_url: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS","kafka:9092")

settings = Setting()
