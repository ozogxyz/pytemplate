import pytest
from hydra import compose, initialize
from hydra.core.global_hydra import GlobalHydra
from omegaconf import DictConfig, open_dict


@pytest.fixture(scope="package")
def cfg_train() -> DictConfig:
    with initialize(version_base="1.2", config_path="../config"):
        cfg = compose(
            config_name="train.yaml", return_hydra_config=True, overrides=[]
        )

    return cfg