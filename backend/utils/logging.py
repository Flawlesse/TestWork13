import logging
from config import settings


logging.basicConfig()

logger = logging.getLogger("FastAPIApp ")
logger.setLevel(logging.DEBUG if settings.app_settings.debug else logging.INFO)
