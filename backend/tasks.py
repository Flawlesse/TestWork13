from celery_app import app
import logging
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


@app.task
def parse_quotes(email, order_id, item, status): ...
