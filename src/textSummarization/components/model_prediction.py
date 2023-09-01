from datasets import load_dataset, load_from_disk
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline
import torch
from textSummarization.entity import ModelPredictionConfig

class ModelPrediction:
    def __init__(self, config: ModelPredictionConfig):
        self.config = config
        self.gen_kwargs = {"length_penalty": config.length_penalty, "num_beams": config.num_beams, "max_length": config.max_length}


    def predict(self, text):

        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
        
        sample_text = text
        #pipelining

        pipe = pipeline("summarization", model=model_pegasus, tokenizer=tokenizer)
        gen_text = pipe(sample_text, **self.gen_kwargs)[0]["summary_text"]

        return gen_text