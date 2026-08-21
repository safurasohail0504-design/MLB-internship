import logging
from pathlib import Path
from datetime import datetime

# Create logs directory
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Configure logging
log_file = LOGS_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_request(request_id, event):
    """Log API request events"""
    logger.info(f"[{request_id}] {event}")

def log_error(request_id, error):
    """Log API errors"""
    logger.error(f"[{request_id}] {error}")

def log_warning(request_id, warning):
    """Log API warnings"""
    logger.warning(f"[{request_id}] {warning}")