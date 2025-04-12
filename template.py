import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: - %(levelname)s - %(message)s')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/tests/__init__.py",
    f"src/{project_name}/tests/test.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent

    # Create directories if they don't exist
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Creating directory: {file_dir}")

    # Create empty files if they don't exist
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists:{file_path}")