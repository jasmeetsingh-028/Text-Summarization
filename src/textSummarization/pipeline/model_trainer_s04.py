from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.model_trainer import ModelTrainer
from textSummarization.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e