import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from typing import Optional

@ensure_annotations
def read_yaml(path_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    
    Args:
        path_yaml (str): Path to the YAML file.

    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object    
    """
    try:
        with open(path_yaml, 'r') as yaml_file:
            return ConfigBox(yaml.safe_load(yaml_file))
            logger.info(f"YAML file: {path_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Invalid YAML format: {e}")
    except Exception as e:
        raise 


def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Create list of directories.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory: {path} created successfully")
        except FileExistsError:
            logger.warning(f"Directory: {path} already exists")
        except Exception as e:
            logger.error(f"Error creating directory: {path} - {e}")
            raise e    


@ensure_annotations
def get_size(path: str) -> str:
    """
    Get the size of a file in KB.

    Args:
        path (str): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"
