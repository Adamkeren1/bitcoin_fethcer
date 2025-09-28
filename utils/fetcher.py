import requests
from utils.logger import Logger
from config import BITCOIN_API_URL


class BitcoinPriceFetcher:
    def __init__(self, logger: Logger):
        self.api_url = BITCOIN_API_URL
        self.logger = logger

    def fetch_price(self):
        try:
            self.logger.debug("Starting Bitcoin price fetch...")  # Debug info
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            price = float(data['data']['amount'])
            assert isinstance(price, float), "Fetched price is not a float"
            self.logger.info(f"Fetched Bitcoin price: {price} USD")  # Success
            return price
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network error fetching Bitcoin price: {e}")  # Error
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error fetching Bitcoin price: {e}")  # Error
            return None
