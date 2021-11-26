import logging.config
import yaml

logger = logging.getLogger()


def init_config():
    """Get configuration variables for the app"""
    filepath = "config/config.yaml"
    config = None
    with open(filepath) as file_stream:
        config = yaml.full_load(file_stream)

    logging.config.dictConfig(config.get("logging"))
    logger.debug("starting config...")
    return config


config = init_config()