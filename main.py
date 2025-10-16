from utils.logger import Logger # Import Logger Class
from utils.fetcher import BitcoinPriceFetcher # Import BitcoinPriceFetcher Class
from utils.data_collector import DataCollector # Import DataCollector Class
from utils.grapher import Grapher  # Import Grapher Class
from utils.emailer import Emailer  # Import Emailer Class
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, RECIPIENT_EMAIL


def main():
    """Main function to orchestrate the Bitcoin price monitoring workflow."""
    try:
        # Instantiate the classes and run the tasks
        logger = Logger(name='MainLogger')
        fetcher = BitcoinPriceFetcher(logger=logger)
        collector = DataCollector(fetcher=fetcher, logger=logger)
        
        # Collect data for one hour
        collector.collect_for_one_hour()
        
        # Create and generate graph
        grapher = Grapher(logger=logger)
        grapher.plot_bpi()
        
        # Send email report
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
        
        logger.info("Bitcoin price monitoring completed successfully!")
        
    except Exception as e:
        if 'logger' in locals():
            logger.error(f"An error occurred: {e}")
        else:
            print(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
