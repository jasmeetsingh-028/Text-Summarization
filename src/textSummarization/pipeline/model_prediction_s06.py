from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.model_prediction import ModelPrediction
from textSummarization.logging import logger

class ModelPredictionPipeline:
    def __init__(self, text):
        self.text = text

    def main(self):
        try:
            config = ConfigurationManager()
            model_pred_config = config.get_model_prediction_config()
            prediction = ModelPrediction(config=model_pred_config)
            output_text = prediction.predict(text =  self.text)
            return output_text
        except Exception as e:
            raise e