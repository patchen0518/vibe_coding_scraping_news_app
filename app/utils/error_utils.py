"""
Error logging utility for scrapers.
"""
import os
from datetime import datetime

ERROR_LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.error_log'))

def log_scraper_error(source: str, message: str) -> None:
    """
    Log a scraping error to the error log directory.

    Args:
        source (str): News source name.
        message (str): Error message.
    """
    os.makedirs(ERROR_LOG_DIR, exist_ok=True)
    log_file = os.path.join(ERROR_LOG_DIR, f"{source.lower()}_errors.log")
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().isoformat()}Z] {message}\n")
