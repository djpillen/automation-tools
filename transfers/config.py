import configparser
import os


def parse_config():
    settings = {}
    default_config = os.path.join(os.path.expanduser("~"), ".automation-tools")
    config = configparser.RawConfigParser()
    config.read(default_config)

    settings = {
        "am_user": config.get("credentials", "am_user"),
        "am_api_key": config.get("credentials", "am_api_key"),
        "ss_user": config.get("credentials", "ss_user"),
        "ss_api_key": config.get("credentials", "ss_api_key"),
        "databasefile": config.get("defaults", "databasefile"),
        "logfile": config.get("defaults", "logfile"),
        "pidfile": config.get("defaults", "pidfile"),
        "scriptextensions": config.get("defaults", "scriptextensions"),
        "processing_config": config.get("defaults", "processing_config"),
        "log_level": config.get("defaults", "log_level"),
        "transfer_type": config.get("defaults", "transfer_type"),
        "am_url": config.get("urls", "am_url"),
        "ss_url": config.get("urls", "ss_url")
    }

    for key, value in config.items("ts_locations"):
        settings[key] = value

    return settings
