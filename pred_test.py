from textSummarization.logging import logger 

from textSummarization.pipeline.model_prediction_s06 import ModelPredictionPipeline


EXP_NAME = "Model prediction step"
try:
   logger.info(f">>>>>> Experiment {EXP_NAME} started <<<<<<") 
   text  = "The schematic diagram provides an overview of how the Text Summarization Streamlit Application functions, from user input to the generation of high-quality summaries, all while maintaining ethical and user-friendly principles.This final product prototype embodies our commitment to delivering a valuable and accessible text summarization tool to a wide range of users, revolutionizing the way they extract insights and knowledge from extensive textual content."
   pred = ModelPredictionPipeline(text = text)
   model_output  = pred.main()
   logger.info(f">>>>>> Experiemnt {EXP_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e