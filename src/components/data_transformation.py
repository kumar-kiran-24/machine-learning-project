import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Fix typo in import: should be DataIngestion not DataIngetion
from src.components.data_ingestion import DataIngetion, DataIngestionConfig

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# Remove unnecessary sys.path.append if your project is set up as a package

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")  # Fix typo in filename

class DataTransformation:
    def __init__(self):
       
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation (returns a preprocessor pipeline)
        '''
        try:
            numerical_features = ["reading_score", "writing_score"]
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehotencoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))  # scaler with_mean=False for sparse data
            ])

            logging.info("Categorical columns encoding completed")
            logging.info("Numerical columns encoding completed")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining the preprocessor object")

            preprocessor_object = self.get_data_transformer_object()

            target_column_name = "math_score"
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing dataframes")

            input_feature_train_arr = preprocessor_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]  # fix: was input_feature_train_arr

            logging.info("Saved preprocessing objects")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_object
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngetion()  # Fixed typo in class name
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
