import os
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = bool(os.environ.get("DEBUG") not in ("false", "False", "0", "f", "F"))
print(f"{DEBUG=}\n{BASE_DIR=}")


class DatabaseSettings(BaseSettings):
    mongo_host: str
    mongo_dbname: str
    mongo_initdb_root_username: str
    mongo_initdb_root_password: str


class AppSettings(BaseSettings):
    debug: bool = DEBUG
    timezone: str = "Europe/Moscow"
    base_dir: Path = BASE_DIR


class RedisSettings(BaseSettings):
    redis_host: str


class Settings(BaseSettings):
    db_settings: DatabaseSettings = DatabaseSettings()
    app_settings: AppSettings = AppSettings()
    redis_settings: RedisSettings = RedisSettings()


settings = Settings()
