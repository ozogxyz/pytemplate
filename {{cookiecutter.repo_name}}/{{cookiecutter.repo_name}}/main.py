import hydra
from omegaconf import DictConfig


@hydra.main(version_base="1.2", config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(omegaconf.OmegaConf.to_yaml(cfg))

if __name__ == "__main__": main()