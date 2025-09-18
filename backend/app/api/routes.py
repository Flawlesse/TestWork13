from fastapi import APIRouter, Depends
from typing import Annotated
from pymongo.asynchronous.client_session import AsyncClientSession

from backend.utils import get_mongodb_async_session
from backend.celery_tasks import parse_quotes

router = APIRouter(
    prefix="/api",
    tags=["Quotes API"],
)


@router.post("/parse-quotes-task")
async def run_quotes_parsing():
    """Runs quote parsing in background with Celery."""

    task = parse_quotes.delay()
    task_id = task.id
    return {"task_id": task_id}


@router.get("/quotes")
async def get_quotes_route(
    session: Annotated[AsyncClientSession, Depends(get_mongodb_async_session)],
):
    pass
