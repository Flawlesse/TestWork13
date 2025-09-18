from fastapi import APIRouter

from utils import logger, get_db
from celery_tasks import parse_quotes
from app.api import schemas


router = APIRouter(
    prefix="/api",
    tags=["Quotes API"],
)


@router.post("/parse-quotes-task")
async def run_quotes_parsing():
    """Run quote parsing in background with Celery."""

    task = parse_quotes.delay()
    task_id = task.id
    logger.info("Successfully ran parsing quotes task in background.")
    return {"task_id": task_id}


@router.get("/quotes", response_model=list[schemas.QuoteResponseSchema])
async def get_quotes_route():
    """Retrieve list of quotes."""
    _db = get_db()
    quotes_coll = _db.quotes

    result = []
    async with quotes_coll.find() as cursor:
        async for doc in cursor:
            result.append(schemas.QuoteResponseSchema(**doc))
    return result if result else {"detail": "No quotes matching your filters!"}
