from textSummarization.logging import logger    #already installed when running setup.py SRC_REPO

#textSummarization is my local package
#testing data_ingestion pipeline

from textSummarization.pipeline.data_ingestion_s01 import DataIngestionTrainingPipeline
from textSummarization.pipeline.data_validation_s02 import DataValidationTrainingPipeline
from textSummarization.pipeline.data_transformation_s03 import DataTransformationTrainingPipeline
from textSummarization.pipeline.model_trainer_s04 import ModelTrainerPipeline

EXP_NAME = "Data Ingestion step"
try:
   logger.info(f">>>>>> Experiment {EXP_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Experiemnt {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

EXP_NAME = "Data Validation step"
try:
   logger.info(f">>>>>> step {EXP_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> step {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

EXP__NAME = "Data Transformation step"
try:
   logger.info(f">>>>>> step {EXP_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> step {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

EXP__NAME = "Data Transformation step"
try:
   logger.info(f">>>>>> step {EXP_NAME} started <<<<<<") 
   data_transformation = ModelTrainerPipeline()
   data_transformation.main()
   logger.info(f">>>>>> step {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


