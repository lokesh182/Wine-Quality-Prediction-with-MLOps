import os 
from WineQPrediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from WineQPrediction.entity.config_entity import DataTransformationConfig

from imblearn.over_sampling import SMOTE

class DataTransformation:
    
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        
    def feature_selection(self) -> pd.DataFrame:
        data = pd.read_csv("data-cleaned.csv")
        
        print(data['quality'].unique())
        
        #if wine quality is 7 or above then we will consider it as good(1) else bad(0)
        data['quality'] = data['quality'].apply(lambda x: 1 if x >= 7 else 0)
        
        print(f"No of good vs bad vine Samples :{data['good_quality'].value_counts()}")
        
        return data
       
    
    def train_test_splitting(self):
        data1 = self.feature_selection()
        X = data1[['fixed acidity', 'volatile acidity', 'sulphates', 'alcohol', 'density']]
        y = data1.quality
        oversample = SMOTE()
        X_ros, y_ros = oversample.fit_resample(X, y)

        sns.countplot(x=y_ros)
        plt.xticks([0,1], ['bad wine','good wine'])
        plt.title("Types of Wine")
         # Specify the directory path to save the graph
        directory_path = "Visualization/images"
        file_name = "wine_quality.png"
        file_path = os.path.join(directory_path, file_name)
        # Save the graph to the specified directory
        plt.savefig(file_path)

        plt.show()
       
        df_rejoined = pd.concat([X_ros, y_ros], axis=1)
        
        data1 = self.feature_selection()
        
        train , test = train_test_split(data1)
        
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'),index=False)
        
        
        logger.info(f"Train and Test data saved at {self.config.root_dir}")
        logger.info(f"Train_data:{train.shape}")
        logger.info(f"Test_data:{test.shape}")
        
 
    
        
        
        