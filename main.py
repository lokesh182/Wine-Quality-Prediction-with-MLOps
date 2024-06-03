from WineQPrediction import logger
from WineQPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQPrediction.pipeline.stage_03_data_transformation import DataTransformationPipeline
from WineQPrediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from WineQPrediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import os
os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/lokesh182/Wine-Quality-Prediction-with-MLOps.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'lokesh182'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'e68300de3f8962945dc7eed134b90856acc5a5b7'
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


STAGE_NAME = "MODEL TRAINER STAGE"
try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed")
    
except Exception as e:
        logger.exception(e)
        raise(e)



STAGE_NAME  = "MODEL EVALUATION STAGE"

try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed")
    
except Exception as e:
        logger.exception(e)
        raise(e)