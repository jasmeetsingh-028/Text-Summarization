FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate


EXPOSE 8501
CMD ["streamlit", "run", "streamlit_application.py"]

#docker run -p 8501:8501 text-summarization-app
#This command will run the Docker container and expose port 8501, which is the default port used by Streamlit applications. You can then access your Streamlit application by navigating to http://localhost:8501 in your web browser.