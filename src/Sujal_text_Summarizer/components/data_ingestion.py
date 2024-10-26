import os
import urllib.request as request
import zipfile
from Sujal_text_Summarizer.utils.common import get_size
from Sujal_text_Summarizer.logging import logger
from pathlib import Path
from Sujal_text_Summarizer.entity import DataingestionConfig

class DataIngestion:
    def __init__(self, config: DataingestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded with the following info: \n{headers}")
            except Exception as e:
                logger.error(f"Failed to download file: {e}")
                raise e
        else:
            logger.info(f"File already exists: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified unzip directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extraction completed at: {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Error: File is not a zip file or it is corrupted: {e}")
            raise e
