from WineQPrediction import logger
from WineQPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA INGESTION STAGE"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e


logger.info("Welcome to custom logger")
""