import pytest
from hydra import compose, initialize

@pytest.fixture(scope="session")
def cfg():
    with initialize(config_path="../configs"):
        return compose(config_name="config")
