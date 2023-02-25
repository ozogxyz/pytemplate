from omegaconf import DictConfig


def test_config(cfg_train: DictConfig):
    assert cfg_train
