import logging.config
import yaml



def init_config():
    """Get configuration variables for the app"""
    filepath = "config/config.yaml"
    config = None
    with open(filepath) as file_stream:
        config = yaml.full_load(file_stream)
    return config


config = init_config()