import time 
import json  
from datetime import datetime
from utils.fetcher import BitcoinPriceFetcher
from utils.logger import Logger

class DataCollector:
    def __init__(self, fetcher: BitcoinPriceFetcher, logger: Logger, json_file='bitcoin_prices.json'):
        self.fetcher = fetcher
        self.logger = logger
        self.json_file = json_file
        self.data = []

    def collect_for_one_hour(self):
        self.logger.log("Starting data collection for one hour.")
        for _ in range(60):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                price = self.fetcher.fetch_price()
                if price is not None:
                    entry = {"timestamp": timestamp, "price": price}
                    self.data.append(entry)
                    self.logger.log(f"Saved price at {timestamp}: {price} USD")
                else:
                    self.logger.log(f"Failed to fetch price at {timestamp}")
                time.sleep(60)
            except Exception as e:
                self.logger.log(f"Exception during price fetch or sleep at {timestamp}: {e}")
        self.save_to_json()

    def save_to_json(self):
        try:
            with open(self.json_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            self.logger.log(f"Saved all collected data to {self.json_file}")
        except Exception as e:
            self.logger.log(f"Failed to save data to {self.json_file}: {e}")