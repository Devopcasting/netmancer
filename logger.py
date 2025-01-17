import logging
from logging.handlers import RotatingFileHandler

LOG_FILE = "/var/log/netmancer.log"

class NetmancerLogger:
    def __init__(self):
        # Set up logging with rotating file handler to prevent the log from growing indefinitely
        handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)  # 5 MB file size, keep 5 backups
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        
        # Add handler to the logger
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        
        # Optionally log to the console as well
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(console_handler)

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)

    def log_warning(self, message):
        logging.warning(message)
