import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo

from backend.celery_app.celery_app import app
from backend.db import db_helper
from backend.config import settings
from backend.utils import logger


class ParsingError(Exception):
    pass


@app.task
def parse_quotes():
    """Quote parsing callback."""

    db = db_helper.sync_client[settings.db_settings.mongo_dbname]

    try:
        response = requests.get("https://quotes.toscrape.com/")
        if response.status_code >= 400:
            message = (
                "https://quotes.toscrape.com/ is non-parsable. "
                + f"Status={response.status_code}."
            )
            raise ParsingError(message)

        # get page layout
        soup = BeautifulSoup(response.text, "lxml")
        quote_blocks = soup.find_all("div", class_="quote")

        parsed_quotes = []
        for q_block in quote_blocks:
            item = {}
            item["quote"] = q_block.find("span", class_="text").text.strip()
            item["author"] = q_block.find("small", class_="author").text.strip()
            item["tags"] = [
                tag.text.strip() for tag in q_block.find_all("a", class_="tag")
            ]
            item["tags"].sort()
            item["additionDate"] = datetime.now(
                ZoneInfo(settings.app_settings.timezone)
            ).date
            parsed_quotes.append(item)

        # store in db
        db.quotes.insert_many(parsed_quotes)
    except Exception as e:
        logger.error(str(e))
        raise e
