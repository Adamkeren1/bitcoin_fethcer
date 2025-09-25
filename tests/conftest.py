import pytest
from utils.logger import Logger

@pytest.fixture
def logger():
    return Logger(name='TestLogger')