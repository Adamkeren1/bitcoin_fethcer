import json  # For reading the JSON data file
import matplotlib.pyplot as plt  # For plotting the graph
from utils.logger import Logger  # Import the Logger class

class Grapher:
    def __init__(self, logger: Logger):
        self.logger = logger  # Store the logger instance for logging actions

    def plot_bpi(self, json_file='bitcoin_prices.json', image_file='bitcoin_bpi.png'):
        # Read the collected data from the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)
        # Extract timestamps and prices from the data
        timestamps = [entry['timestamp'] for entry in data]
        prices = [entry['price'] for entry in data]

        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, prices, marker='o')
        plt.xlabel('Timestamp')
        plt.ylabel('Bitcoin Price (USD)')
        plt.title('Bitcoin Price Index (BPI) Over 1 Hour')
        # Show every 5th label only
        step = max(1, len(timestamps) // 12)  # Show about 12 labels
        plt.xticks(ticks=range(0, len(timestamps), step), labels=[timestamps[i] for i in range(0, len(timestamps), step)], rotation=45)
        plt.tight_layout()
        plt.savefig(image_file)
        plt.close()
        self.logger.log(f"Graph saved as {image_file}")