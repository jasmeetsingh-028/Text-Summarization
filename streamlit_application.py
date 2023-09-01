import streamlit as st
from textSummarization.pipeline.model_prediction_s06 import ModelPredictionPipeline

# Function to generate summary using the model
def generate_summary(text):
    pred = ModelPredictionPipeline(text=text)
    model_output = pred.main()
    return model_output

# Streamlit UI
st.title("Text Summarization App")

# Create a sidebar for description and GitHub link
st.sidebar.title("About")
st.sidebar.write(
    "This Text Summarization App allows you to generate summaries from input text. "
)
st.sidebar.write("Author: Jasmeet Singh")
st.sidebar.write("[GitHub Profile](https://github.com/jasmeetsingh-028)")

# User input text area
user_input = st.text_area("Input Text", "")

# Generate summary when the user clicks the button
if st.button("Generate Summary"):
    if user_input.strip() == "":
        st.warning("Please enter some text to generate a summary.")
    else:
        summary = generate_summary(user_input)
        print('Summary generated')
        st.write(summary)

# Separate box for displaying the model-generated summary
