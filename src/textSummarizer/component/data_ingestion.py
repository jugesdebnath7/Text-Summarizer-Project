import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                file_name, _ = request.urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )
                logger.info(f"{file_name} downloaded successfully")
            else:
                logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")
        except request.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err.code} - {http_err.reason}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise 
        

    def extract_zip_file(self):
        """
        Extracts the zip file to the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            logger.info(f"Extracting file: {self.config.local_data_file}")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Bad ZIP file: {e}")
            raise e
        except Exception as e:
            logger.error(f"An unexpected error occurred during extraction: {e}", exc_info=True)
            raise e

   