import pytest
from hydra import compose, initialize
from omegaconf import DictConfig


# Set config.yaml as default config for all tests
@pytest.fixture(scope="package")
def train_config() -> DictConfig:
    with initialize(version_base="1.2", config_path="../conf"):
        # use default config as defaults for all tests
        cfg = compose(
            config_name="config.yaml", return_hydra_config=True, overrides=[]
        )

    return cfg