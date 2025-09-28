import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.fetcher import BitcoinPriceFetcher

def test_fetch_price_returns_float(caplog, logger):
    with caplog.at_level(logging.INFO):  # Capture INFO and above
        fetcher = BitcoinPriceFetcher(logger=logger)
        price = fetcher.fetch_price()
        
        # Test the return value
        assert price is None or isinstance(price, float)
        
        # Test logging behavior with levels
        if price is not None:
            assert "Fetched Bitcoin price" in caplog.text
            # Check that it was logged at INFO level
            assert any(record.levelname == 'INFO' for record in caplog.records)
        else:
            # Check that errors are logged at ERROR level
            assert any(record.levelname == 'ERROR' for record in caplog.records)
