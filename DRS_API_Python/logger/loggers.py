import logging
import sys
import os
from logging import config

logger_ini_file_path="C:\\Users\\csand\\Desktop\\DRS_API_Python\\logger\\logging.ini"

def setup_logging(config_file=logger_ini_file_path):
    """Initialize logging configuration from a file."""
    if not os.path.exists(config_file):
        print(f"Error: Logging configuration file '{config_file}' not found.")
        return
    try:
        config.fileConfig(config_file)
    except Exception as e:
        print(f"Error setting up logging: {e}")

def get_logger(logger_name):
    """Retrieve a logger by name."""
    return logging.getLogger(logger_name)

# Setup logging on module import
setup_logging()