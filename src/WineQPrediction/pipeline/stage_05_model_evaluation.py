from WineQPrediction.config.configuration import ConfigurationManager
from WineQPrediction.components.model_evaluation import ModelEvaluation
from WineQPrediction import logger

STAGE_NAME  = "MODEL EVALUATION STAGE"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed")
    
    except Exception as e:
        logger.exception(e)
        raise(e)