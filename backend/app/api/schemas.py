from pydantic import BaseModel
from datetime import date


class QuoteResponseSchema(BaseModel):
    quote: str
    author: str
    tags: list[str]
    additionDate: date
