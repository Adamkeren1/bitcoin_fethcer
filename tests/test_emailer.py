import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.emailer import Emailer
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, RECIPIENT_EMAIL





def test_send_bpi_report(logger):
    emailer = Emailer(
        logger=logger,
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        username=SMTP_USERNAME,
        password=SMTP_PASSWORD
    )
   
    try:
        emailer.send_bpi_report(
            json_file='bitcoin_prices.json',
            image_file='bitcoin_bpi.png',
            recipient_email=RECIPIENT_EMAIL
        )
    except Exception as e:
        logger.fail(f"Email sending failed: {e}")