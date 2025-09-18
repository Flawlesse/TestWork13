import fastapi
from contextlib import asynccontextmanager

from db import db_helper
from app.api import router as api_router
from utils import logger


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    logger.info("Trying to ping MongoDB...")
    try:
        await db_helper.async_client.admin.command("ping")
        logger.info("MongoDB is fully acessible! Setting up DB collections...")
        try:
            db_helper.prepare_db()
        except Exception as e:
            logger.warning(str(e))
        logger.info("DB collections have been set up successfully!")
        yield  # app runs here
    except Exception as e:
        logger.error(f"Pigning MongoDB failed: {e}")

    finally:
        logger.info("Closing MongoDB connection...")
        await db_helper.dispose()
        logger.info("MongoDB connection closed.")


app = fastapi.FastAPI(lifespan=lifespan)
app.include_router(api_router)
