from utils.logger import Logger # Import Logger Class
from utils.fetcher import BitcoinPriceFetcher # Import BitcoinPriceFetcher Class
from utils.data_collector import DataCollector # Import DataCollector Class
from utils.grapher import Grapher  # Import Grapher Class
from utils.emailer import Emailer  # Import Emailer Class
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, RECIPIENT_EMAIL


#instantiate the classes and run the tasks
logger = Logger(name='MainLogger')
fetcher = BitcoinPriceFetcher(logger=logger)
collector = DataCollector(fetcher=fetcher, logger=logger)
collector.collect_for_one_hour()  # This will run for 1 hour and save the data to bitcoin_prices.json

grapher = Grapher(logger=logger)  # 2. Create Grapher instance
grapher.plot_bpi()

emailer = Emailer(
    logger=logger,
    smtp_server=SMTP_SERVER,
    smtp_port=SMTP_PORT,
    username=SMTP_USERNAME,
    password=SMTP_PASSWORD
)

emailer.send_bpi_report(
    json_file='bitcoin_prices.json',
    image_file='bitcoin_bpi.png',
    recipient_email=RECIPIENT_EMAIL
)