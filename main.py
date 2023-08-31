from textSummarization.logging import logger    #already installed when running setup.py SRC_REPO

#textSummarization is my local package
#testing data_ingestion pipeline

from textSummarization.pipeline.data_ingestion_s01 import DataIngestionTrainingPipeline

EXP_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> Experiment {EXP_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Experiemnt {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e