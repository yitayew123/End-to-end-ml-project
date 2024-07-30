# Import the operating system interface module
import os
# Import BoxValueError exception from box library
from box.exceptions import BoxValueError
# Import yaml module to handle YAML files
import yaml
# Import the logger from the mlProject module
from mlProject import logger
# Import the JSON module to handle JSON files
import json
# Import the joblib module for saving and loading binary files
import joblib
# Import ensure_annotations decorator from ensure module for type checking
from ensure import ensure_annotations
# Import ConfigBox class from box module
from box import ConfigBox
# Import Path class from pathlib module for filesystem paths
from pathlib import Path
# Import Any type from typing module for type hints
from typing import Any

# Function to read a YAML file and return its content as a ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        # Open the YAML file
        with open(path_to_yaml) as yaml_file:
            # Load the content of the YAML file
            content = yaml.safe_load(yaml_file)
            # Log the successful loading of the YAML file
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # Return the content as a ConfigBox object
            return ConfigBox(content)
    except BoxValueError:
        # Raise ValueError if the YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Raise any other exceptions
        raise e

# Function to create directories from a list of paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    # Iterate over the list of directory paths
    for path in path_to_directories:
        # Create directories, do not raise an error if they already exist
        os.makedirs(path, exist_ok=True)
        # Log the creation of each directory if verbose is True
        if verbose:
            logger.info(f"created directory at: {path}")

# Function to save data to a JSON file
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    # Open the JSON file in write mode
    with open(path, "w") as f:
        # Dump the data into the JSON file with indentation
        json.dump(data, f, indent=4)
    # Log the successful saving of the JSON file
    logger.info(f"json file saved at: {path}")

# Function to load data from a JSON file and return as a ConfigBox
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    # Open the JSON file
    with open(path) as f:
        # Load the content of the JSON file
        content = json.load(f)
    # Log the successful loading of the JSON file
    logger.info(f"json file loaded succesfully from: {path}")
    # Return the content as a ConfigBox object
    return ConfigBox(content)

# Function to save data to a binary file
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    # Dump the data into the binary file
    joblib.dump(value=data, filename=path)
    # Log the successful saving of the binary file
    logger.info(f"binary file saved at: {path}")

# Function to load data from a binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    # Load the data from the binary file
    data = joblib.load(path)
    # Log the successful loading of the binary file
    logger.info(f"binary file loaded from: {path}")
    # Return the loaded data
    return data

# Function to get the size of a file in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    # Get the size of the file in bytes and convert to KB
    size_in_kb = round(os.path.getsize(path) / 1024)
    # Return the size in KB as a string
    return f"~ {size_in_kb} KB"

