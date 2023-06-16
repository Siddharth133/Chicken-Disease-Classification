from CNN_CLASSIFIER.config.configuration import ConfigurationManager
from CNN_CLASSIFIER.components.data_ingestion import DataIngestion
from CNN_CLASSIFIER import logger
import os
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        # Perform the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<\n\nx===========x")

    except Exception as e:
        # Log any exceptions that occur during execution
        logger.exception(e)
        raise e
