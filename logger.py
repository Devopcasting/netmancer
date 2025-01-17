import logging
from logging.handlers import RotatingFileHandler

LOG_FILE = "/var/log/netmancer.log"

class NetmancerLogger:
    def __init__(self):
        # Create a logger instance
        self.logger = logging.getLogger("NetmancerLogger")

        # Check if the logger already has handlers to prevent adding multiple handlers
        if not self.logger.hasHandlers():
            # Set up logging with rotating file handler to prevent the log from growing indefinitely
            handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)  # 5 MB file size, keep 5 backups
            handler.setLevel(logging.INFO)
            handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

            # Add handler to the logger
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)
