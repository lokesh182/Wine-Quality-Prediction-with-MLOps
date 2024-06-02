import os 
from WineQPrediction import logger
from WineQPrediction.config.configuration import ConfigurationManager
from WineQPrediction.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config:  DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = False
            
            data = pd.read_csv("data-cleaned.csv")
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"validation status: {validation_status}")
                   
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"validation status: {validation_status}")
                    
            return validation_status
        
        except Exception as e:
            raise e