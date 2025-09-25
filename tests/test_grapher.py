import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.grapher import Grapher

def test_plot_bpi_creates_image(logger):
    json_file = 'bitcoin_prices.json'
    image_file = 'test_bitcoin_bpi.png'
    # Skip the test if the JSON file does not exist
    if not os.path.exists(json_file):
        pytest.skip(f"{json_file} does not exist, skipping test.")
    grapher = Grapher(logger=logger)
    grapher.plot_bpi(json_file=json_file, image_file=image_file)
    assert os.path.exists(image_file)
    os.remove(image_file)