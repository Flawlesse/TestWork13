from fastapi import APIRouter, Query
from typing import Annotated
from fastapi.responses import JSONResponse

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
async def get_quotes_route(
    author: Annotated[
        str | None,
        Query(description="Author of the quote."),
    ] = None,
    tags: Annotated[
        list[str] | None,
        Query(alias="tag", description="Tags of the quote."),
    ] = None,
):
    """Retrieve list of quotes."""
    _db = get_db()
    quotes_coll = _db.quotes

    filter_cond = {}
    if author:
        filter_cond["author"] = author.strip()
    if tags:
        filter_cond["tags"] = {"$in": tags}

    logger.info(f"Filtering quotes by conditions:\n{filter_cond}")
    result = []
    async with quotes_coll.find(filter_cond) as cursor:
        async for doc in cursor:
            result.append(schemas.QuoteResponseSchema(**doc))

    if not result:
        return JSONResponse(
            {"detail": "No quotes matching your filters!"},
            status_code=404,
        )
    return result
