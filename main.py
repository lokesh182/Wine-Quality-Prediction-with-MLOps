from WineQPrediction import logger
from WineQPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQPrediction.pipeline.stage_03_data_transformation import DataTransformationPipeline

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

STAGE_NAME = "DATA TRANSFORMATION STAGE"
try:
        logger.info(f"Stage : {STAGE_NAME} started")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f"Stage : {STAGE_NAME} completed")
except Exception as e:
        logger.exception(e)
        raise e
""