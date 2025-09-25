import logging  # Import the built-in logging module for logging messages

class Logger:
    def __init__(self, log_file='bitcoin_price.log', name: str = 'BitcoinLogger'):
        # Create or get a logger named 'BitcoinLogger'
        self.logger = logging.getLogger(name)
        # Set the logging level to INFO (captures info, warning, error, etc.)
        self.logger.setLevel(logging.INFO)
        # Create a file handler to write logs to the specified log file
        fh = logging.FileHandler(log_file)
        # Define the format for log messages (timestamp, level, message)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # Set the formatter for the file handler
        fh.setFormatter(formatter)
        # Add the file handler to the logger if it doesn't already have handlers
        if not self.logger.handlers:
            self.logger.addHandler(fh)

    def log(self, message: str):
        # Log the given message at INFO level
        self.logger.info(message)