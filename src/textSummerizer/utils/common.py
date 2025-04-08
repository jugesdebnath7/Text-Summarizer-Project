import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, List, Dict, Union


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBix object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
         ConfigBox: Contents of the YAML file as a ConfigBox object.     
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose: bool = True) -> None:
    """
    Create list of directories

    Args:
        path_to_directories (list[Path]): List of directories to create.
        verbose (bool): If True, print the directories being created.
        ignore_log (bool, optional): Ignore if multiple directories exist. Defaults to False.

    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory: {path} created successfully")
        except FileExistsError:
            if verbose:
                logger.warning(f"Directory: {path} already exists")
        except Exception as e:
            logger.error(f"Error creating directory: {path} - {e}")
            raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path(Path): Path to the file.

    Returns:
        str: Size of the file in KB.    
    """        
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~ {size_in_kb} KB"
              