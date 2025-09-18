import fastapi
from contextlib import asynccontextmanager

from backend.db import db_helper
from backend.app.api import router as api_router
from backend.utils import logger


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    logger.info("Trying to ping MongoDB...")
    try:
        db_helper.client.admin.command("ping")
        logger.info("MongoDB is fully acessible!")
        yield  # app runs here
    except Exception as e:
        logger.error(f"Pigning MongoDB failed: {e}")
    finally:
        logger.info("Closing MongoDB connection...")
        await db_helper.dispose()
        logger.info("MongoDB connection closed.")


app = fastapi.FastAPI()
app.include_router(api_router)
