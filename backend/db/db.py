from pymongo.asynchronous.mongo_client import AsyncMongoClient
from pymongo.asynchronous.client_session import AsyncClientSession
from pymongo import MongoClient
from typing import AsyncGenerator

from backend.config import settings


CONNECTION_URI = (
    f"mongodb://{settings.db_settings.mongo_initdb_root_username}:"
    + f"{settings.db_settings.mongo_initdb_root_password}@"
    + f"{settings.db_settings.mongo_host}:27017/"
)


class DBHelper:
    def __init__(self) -> None:
        self.async_client = AsyncMongoClient(CONNECTION_URI)
        self.sync_client = MongoClient(CONNECTION_URI)

    async def dispose(self) -> None:
        await self.async_client.close()
        self.sync_client.close()

    async def session_getter(self) -> AsyncGenerator[AsyncClientSession, None]:
        async with self.client.start_session() as session:
            yield session
