import requests
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo

from celery_app.celery_app import app
from db import db_helper
from config import settings
from utils import logger


class ParsingError(Exception):
    pass


@app.task
def parse_quotes():
    """Quote parsing callback."""

    db = db_helper.sync_client[settings.db_settings.mongo_dbname]
    try:
        logger.info("Starting to parse quotes.")
        logger.info("Waiting for response from GET https://quotes.toscrape.com/...")
        response = requests.get("https://quotes.toscrape.com/")
        if response.status_code >= 400:
            message = (
                "https://quotes.toscrape.com/ is non-parsable. "
                + f"Status={response.status_code}."
            )
            raise ParsingError(message)
        logger.info("Got a successful response back! Now, parsing stage.")

        # get page layout
        soup = BeautifulSoup(response.text, "lxml")
        quote_blocks = soup.find_all("div", class_="quote")
        if not quote_blocks:
            raise ParsingError("No quote blocks found.")
        logger.info(f"Found {len(quote_blocks)} quote blocks, retrieving info.")

        parsed_quotes = []
        for q_block in quote_blocks:
            item = {}
            item["quote"] = q_block.find("span", class_="text").text.strip()
            item["author"] = q_block.find("small", class_="author").text.strip()
            item["tags"] = [
                tag.text.strip() for tag in q_block.find_all("a", class_="tag")
            ]
            item["tags"].sort()
            # 1. Consider time zone
            # 2. Get date regarding timezone
            # 3. Transform it back to datetime, since MongoDB does not allow date
            item["additionDate"] = datetime.combine(
                datetime.now(ZoneInfo(settings.app_settings.timezone)).date(),
                datetime.min.time(),
            )
            parsed_quotes.append(item)
        logger.info(f"Collected quotes (size={len(parsed_quotes)}): {parsed_quotes}")

        # store in db
        db.quotes.insert_many(parsed_quotes)
        logger.info(f"Successfully inserted {len(parsed_quotes)} quotes in DB.")
    except Exception as e:
        logger.error(str(e))
        raise e
    logger.info("Parsing finished successfully!")
