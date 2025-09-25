import requests
from utils.logger import Logger
from config import BITCOIN_API_URL


class BitcoinPriceFetcher:
    def __init__(self, logger: Logger):
        self.api_url = BITCOIN_API_URL
        self.logger = logger

    def fetch_price(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            price = float(data['data']['amount'])
            assert isinstance(price, float), "Fetched price is not a float"
            self.logger.log(f"Fetched Bitcoin price: {price} USD")
            return price
        except requests.exceptions.RequestException as e:
            self.logger.log(f"Network error fetching Bitcoin price: {e}")
            return None
        except Exception as e:
            self.logger.log(f"Unexpected error fetching Bitcoin price: {e}")
            return None