from Sujal_text_Summarizer.config.configuration import ConfigurationManager
from Sujal_text_Summarizer.components.data_ingestion import DataIngestion
from Sujal_text_Summarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 
    def main(self):
        config = ConfigurationManager()

        data_injection_config = config.get_data_ingestion_config()  # Ensure this method returns a valid DataIngestionConfig object
        data_injection = DataIngestion(config=data_injection_config)
        data_injection.download_file()
        data_injection.extract_zip_file()