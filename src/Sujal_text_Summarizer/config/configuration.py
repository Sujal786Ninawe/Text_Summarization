from Sujal_text_Summarizer.constants import *
from Sujal_text_Summarizer.utils.common import read_yaml, create_directories
from Sujal_text_Summarizer.entity import (DataingestionConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath= PARAMS_FILE_PATH):
            
            self.config=read_yaml(config_filepath)
            self.params= read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataingestionConfig:
          config = self.config.data_injection

          create_directories([config.root_dir])

          data_injection_config= DataingestionConfig(
                root_dir=config.root_dir,
                source_URL= config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir

          )

          return data_injection_config