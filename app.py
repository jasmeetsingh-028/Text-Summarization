from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import gradio as gr

model_name = "ailm/pegsus-text-summarization"
model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = PegasusTokenizer.from_pretrained(model_name)

def summarize(text):
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    return tokenizer.decode(summary[0], skip_special_tokens=True)

iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch()