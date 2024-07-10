import os  # Importing the os module to interact with the operating system
from pathlib import Path  # Importing Path from pathlib to handle file system paths
import logging  # Importing logging to log messages

# Configuring the logging module to display INFO level messages and specify the message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

# Defining the name of the project
project_name = "mlproject"

# List of files to be created in the project
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

# Loop through each file path in the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object

    filedir, filename = os.path.split(filepath)  # Split the file path into directory and file name

    if filedir != "":  # If the directory part is not empty
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Log directory creation

    # Check if the file does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create the file and open it in write mode
            pass  # Close the file immediately, leaving it empty
            logging.info(f"Creating empty file: {filepath}")  # Log file creation
    else:
        logging.info(f"{filename} already exists")  # Log that the file already exists