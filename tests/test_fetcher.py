from utils.fetcher import BitcoinPriceFetcher
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def test_fetch_price_returns_float(logger):
    fetcher = BitcoinPriceFetcher(logger=logger)
    price = fetcher.fetch_price()
    assert price is None or isinstance(price, float)