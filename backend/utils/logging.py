import logging
from backend.config import settings


logging.basicConfig()

logger = logging.getLogger("FastAPIApp")
logger.setLevel(logging.INFO if settings.app_settings.debug else logging.WARNING)
