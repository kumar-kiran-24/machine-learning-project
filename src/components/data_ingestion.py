import os
import sys
# Incorrect — missing argument, will cause error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass# use for directly define class varible 
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train.csv") # all op store in artificat folder
    test_data_path=os.path.join("artifacts","test.csv") 
    raw_data_path=os.path.join("artifacts","data.csv")

class DataIngetion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
 
    def initiate_data_ingestion(self):
            logging.info("Entered the data ingestion method or componet")
            try:
                df=pd.read_csv("notebook/data/stud.csv")
                logging.info("Read the data set as data frame")

                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)# save the raw data path
                logging.info("Train test split inittiated")
                train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
                train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

                test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

                logging.info("Ingestion of the data is completed")
                return(
                     self.ingestion_config.train_data_path,
                     self.ingestion_config.test_data_path,

                )

            except Exception as e:
                raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngetion()  # if you're keeping the typo class name
    obj.initiate_data_ingestion()