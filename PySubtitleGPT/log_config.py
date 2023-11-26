import logging
from logging.handlers import RotatingFileHandler
import datetime


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Capture all logs

    # Generate a timestamped filename for the log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"debug_logs_{timestamp}.log"

    # Debug log file handler
    debug_file_handler = RotatingFileHandler(log_filename, maxBytes=5 * 1024 * 1024, backupCount=2)
    debug_file_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s:%(lineno)d(%(funcName)s) - %(levelname)s - %(message)s')
    debug_file_handler.setFormatter(debug_formatter)
    logger.addHandler(debug_file_handler)

    # Console handler for info and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
