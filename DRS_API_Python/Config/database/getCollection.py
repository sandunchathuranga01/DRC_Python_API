import configparser
import os

def get_collection_name(collection_key):
    config_path = os.path.join(os.path.dirname(__file__), "DB_Config.ini")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config['COLLECTIONS'].get(collection_key, collection_key)