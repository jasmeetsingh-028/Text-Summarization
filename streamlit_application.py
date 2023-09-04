import streamlit as st
from textSummarization.pipeline.model_prediction_s06 import ModelPredictionPipeline

st.set_page_config(layout="wide")

# Function to generate summary using the model
def generate_summary(text):
    pred = ModelPredictionPipeline(text=text)
    model_output = pred.main()
    print(f'Model Output: {model_output}')
    return model_output


st.subheader("Summarize your Text")
input_text = st.text_area("Enter your text here")
if input_text is not None:
    if st.button("Summarize Text"):
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("**Your Input Text**")
            st.info(input_text)
        with col2:
            st.markdown("**Summary Result**")
            result = generate_summary(input_text)
            st.success(result)

