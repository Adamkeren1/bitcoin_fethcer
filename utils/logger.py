import logging  # Import the built-in logging module for logging messages

class Logger:
    def __init__(self, log_file='bitcoin_price.log', name: str = 'BitcoinLogger', level=logging.INFO):
        # Create or get a logger named 'BitcoinLogger'
        self.logger = logging.getLogger(name)
        # Set the logging level to the specified level (default: INFO)
        self.logger.setLevel(level)
        
        # Create file handler
        fh = logging.FileHandler(log_file)
        # Define the format for log messages (timestamp, level, message)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # Set the formatter for the file handler
        fh.setFormatter(formatter)
        
        # Add the file handler to the logger if it doesn't already have handlers
        if not self.logger.handlers:
            self.logger.addHandler(fh)

    def info(self, message: str):
        # Log the given message at INFO level
        self.logger.info(message)
    
    def warning(self, message: str):
        # Log the given message at WARNING level
        self.logger.warning(message)
    
    def error(self, message: str):
        # Log the given message at ERROR level
        self.logger.error(message)
    
    def debug(self, message: str):
        # Log the given message at DEBUG level
        self.logger.debug(message)
    
    # Keep the old method for backward compatibility
    def log(self, message: str):
        # Log the given message at INFO level
        self.logger.info(message)
