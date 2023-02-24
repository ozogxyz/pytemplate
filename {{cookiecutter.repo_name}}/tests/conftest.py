import pytest
from hydra import compose, initialize
from omegaconf import DictConfig


@pytest.fixture(scope="package")
def cfg_train() -> DictConfig:
    with initialize(version_base="1.2", config_path="../config"):
        cfg = compose(
            config_name="config.yaml", return_hydra_config=True, overrides=[]
        )

    return cfg
