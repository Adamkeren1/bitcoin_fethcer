import json  # For reading the JSON data file
import matplotlib.pyplot as plt  # For plotting the graph
from utils.logger import Logger  # Import the Logger class

class Grapher:
    def __init__(self, logger: Logger):
        self.logger = logger  # Store the logger instance for logging actions

    def plot_bpi(self, json_file='bitcoin_prices.json', image_file='bitcoin_bpi.png'):
        try:
            self.logger.info(f"Starting to create graph from {json_file}")
            
            # Load data from JSON
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            if not data:
                self.logger.warning("No data found in JSON file")
                return
            
            # Extract timestamps and prices
            timestamps = [entry['timestamp'] for entry in data]
            prices = [entry['price'] for entry in data]
            
            # Create the plot
            plt.figure(figsize=(12, 6))
            plt.plot(timestamps, prices, marker='o')
            plt.title('Bitcoin Price Index Over Time')
            plt.xlabel('Time')
            plt.ylabel('Price (USD)')
            
            # Show only about 12 time labels for better readability
            step = max(1, len(timestamps) // 12)  # Show about 12 labels
            plt.xticks(range(0, len(timestamps), step), 
                       [timestamps[i] for i in range(0, len(timestamps), step)], 
                       rotation=45)
            
            plt.tight_layout()
            
            # Save the plot
            plt.savefig(image_file)
            plt.close()
            self.logger.info(f"Graph saved as {image_file}")
            
        except FileNotFoundError:
            self.logger.error(f"JSON file {json_file} not found")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in {json_file}: {e}")
        except KeyError as e:
            self.logger.error(f"Missing required key in JSON data: {e}")
        except Exception as e:
            self.logger.error(f"Failed to create graph: {e}")
            # Clean up in case of error
            plt.close()
