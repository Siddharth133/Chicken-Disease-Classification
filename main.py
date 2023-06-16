from CNN_CLASSIFIER.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_CLASSIFIER import logger
STAGE_NAME = 'Date Ingestion stage'
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

