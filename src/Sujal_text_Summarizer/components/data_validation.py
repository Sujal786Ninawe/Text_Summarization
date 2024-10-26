import os 
from Sujal_text_Summarizer.logging import logger
from Sujal_text_Summarizer.entity import DataValidationConfig


class Datavalidation:
    def __init__(self, config : DataValidationConfig):
        self.config =config 

    def validation_all_files_exists(self)-> bool:
        try :
            validation_status =None 
            all_files = os.listdir(os.path.join("artifacts","data_injection","CSV"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status  = False
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write(" Validation status: {validation_status} ")

                else :
                    validation_status= True
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write("validation status :{validation_status}")

            return validation_status
        except Exception as e:
            raise e