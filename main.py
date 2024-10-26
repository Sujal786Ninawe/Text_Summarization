from Sujal_text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Sujal_text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Sujal_text_Summarizer.logging import logger

Stage_Name = " Data Ingestion stage "
try :
    logger.info(f"<<<<<<<<<< stage(Stage_Name)Started>>>>>>>>>>")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>stage(Stage_Name)Completed >>>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e 


Stage_Name = " Data validation stage "
try :
    logger.info(f"<<<<<<<<<< stage(Stage_Name)Started>>>>>>>>>>")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>stage(Stage_Name)Completed >>>>>>>>")

except Exception as e:
    logger.exception(e)
    raise e 