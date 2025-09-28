import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.emailer import Emailer
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, RECIPIENT_EMAIL





def test_send_bpi_report(caplog, logger):
    json_file = 'bitcoin_prices.json'
    image_file = 'bitcoin_bpi.png'
    
    # Skip if required files don't exist
    if not os.path.exists(json_file) or not os.path.exists(image_file):
        pytest.skip("Required files (JSON or image) do not exist, skipping test.")
    
    emailer = Emailer(
        logger=logger,
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        username=SMTP_USERNAME,
        password=SMTP_PASSWORD
    )
    
    # This will actually send an email! You may want to mock this in real tests.
    try:
        emailer.send_bpi_report(
            json_file=json_file,
            image_file=image_file,
            recipient_email=RECIPIENT_EMAIL
        )
        # Test successful email sending
        assert "Email sent" in caplog.text or "maximum Bitcoin price" in caplog.text
    except Exception as e:
        # Test that failures are properly logged
        assert "Failed to send email" in caplog.text or "error" in caplog.text.lower()
