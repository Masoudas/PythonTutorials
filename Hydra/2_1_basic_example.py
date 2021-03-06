"""
We put our configuration file in a conf folder, in a file called config.yaml
Config:

conf/config.yaml
db:
  driver: mysql
  user: omry
  pass: secret

Inside the application, we use the hydra decorator. Notice that the call to main does not pass any params, but the decorator wrapps the main, and then passes the config class.

Notice also that we supply a type to the configuration params (a DictConfig.) We can, of course, create our own data classes, as we discuss next.

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()

"""