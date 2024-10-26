from Sujal_text_Summarizer.config.configuration import ConfigurationManager
from Sujal_text_Summarizer.components.data_validation import Datavalidation
from Sujal_text_Summarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 
    def main(self):
        config = ConfigurationManager()

       
        data_validation_config = config.get_data_validation_config()  # Fixing the variable name
        data_validation = Datavalidation(config=data_validation_config)  # Correctly using data_validation_config
        data_validation.validation_all_files_exists()
