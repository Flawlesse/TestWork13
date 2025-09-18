from db import db_helper
from config import settings


def get_db():
    return db_helper.async_client[settings.db_settings.mongo_dbname]
