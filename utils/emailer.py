import smtplib
import json
from email.message import EmailMessage
from utils.logger import Logger

class Emailer:
    def __init__(self, logger: Logger, smtp_server, smtp_port, username, password):
        self.logger = logger
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_bpi_report(self, json_file, image_file, recipient_email):
        # Read the collected data to find the max price
        with open(json_file, 'r') as f:
            data = json.load(f)
        max_entry = max(data, key=lambda x: x['price'])
        max_price = max_entry['price']
        max_time = max_entry['timestamp']

        # Create the email
        msg = EmailMessage()
        msg['Subject'] = 'Bitcoin Price Report - Last Hour'
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg.set_content(
            f"The maximum Bitcoin price in the last hour was {max_price} USD at {max_time}."
        )

        # Attach the graph image
        try:
            with open(image_file, 'rb') as img:
                msg.add_attachment(img.read(), maintype='image', subtype='png', filename=image_file)
        except Exception as e:
            self.logger.log(f"Failed to attach image {image_file}: {e}")
            return

        # Send the email
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.send_message(msg)
            self.logger.log(f"Email sent to {recipient_email} with max price {max_price} USD.")
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
