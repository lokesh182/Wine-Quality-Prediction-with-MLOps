from WineQPrediction import logger
from WineQPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "DATA VALIDATION STAGE"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e
""