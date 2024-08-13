import os  # Import the OS module for interacting with the operating system
from box.exceptions import BoxValueError  # Import BoxValueError exception from the box library
import yaml  # Import YAML module to handle YAML files
from mlproject import logger  # Import logger from the mlproject module
import json  # Import JSON module to handle JSON files
import joblib  # Import joblib for saving and loading binary files
from ensure import ensure_annotations  # Import ensure_annotations to enforce type annotations
from box import ConfigBox  # Import ConfigBox for handling dictionary-like objects with dot notation
from pathlib import Path  # Import Path class from pathlib to handle file paths
from typing import Any  # Import Any from typing module to allow any type in function arguments and return values

@ensure_annotations  # Decorator to enforce type annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If there is any other error while reading the file.

    Returns:
        ConfigBox: Parsed content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open the YAML file
            content = yaml.safe_load(yaml_file)  # Load the content using safe_load
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log success message
            return ConfigBox(content)  # Return content as a ConfigBox object
    except BoxValueError:  # Catch specific BoxValueError if the file is empty
        raise ValueError("yaml file is empty")  # Raise a ValueError with a custom message
    except Exception as e:  # Catch all other exceptions
        raise e  # Raise the caught exception

@ensure_annotations  # Decorator to enforce type annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, log a message for each created directory. Defaults to True.
    """
    for path in path_to_directories:  # Loop through each path in the list
        os.makedirs(path, exist_ok=True)  # Create directory, do nothing if it already exists
        if verbose:  # If verbose is True
            logger.info(f"created directory at: {path}")  # Log the directory creation

@ensure_annotations  # Decorator to enforce type annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary data to be saved in the JSON file.
    """
    with open(path, "w") as f:  # Open the file for writing
        json.dump(data, f, indent=4)  # Dump the dictionary into the file with indentation

    logger.info(f"json file saved at: {path}")  # Log the file save location

@ensure_annotations  # Decorator to enforce type annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from the JSON file as a ConfigBox object.
    """
    with open(path) as f:  # Open the JSON file for reading
        content = json.load(f)  # Load the content of the file

    logger.info(f"json file loaded successfully from: {path}")  # Log successful load
    return ConfigBox(content)  # Return the content as a ConfigBox object

@ensure_annotations  # Decorator to enforce type annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file.

    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Dump the data as a binary file using joblib
    logger.info(f"binary file saved at: {path}")  # Log the file save location

@ensure_annotations  # Decorator to enforce type annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)  # Load the binary data using joblib
    logger.info(f"binary file loaded from: {path}")  # Log successful load
    return data  # Return the loaded data

@ensure_annotations  # Decorator to enforce type annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB as a string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Get the file size in KB
    return f"~ {size_in_kb} KB"  # Return the size as a formatted string