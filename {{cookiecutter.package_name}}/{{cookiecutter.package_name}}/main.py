import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base="1.2", config_path="../config", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    main()
