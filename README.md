# Text Summarization Streamlit Application
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pnhMW99OsfIlQAc98XCU3MaclwTf6g7P) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jasmeetsingh-028/Text-Summarization/blob/main/LICENSE.md)

This repository contains a Streamlit-based application for text summarization using the "sasum dialogue summarization" dataset and the "google/pegasus-cnn_dailymail" model. The application is divided into different pipeline steps for data ingestion, data validation, data transformation, and model training. Additionally, it uses logging to capture experiment details and errors.

## Application Features

- **Data Ingestion**: Ingest data from the "sasum dialogue summarization" dataset.
- **Data Validation**: Validate and preprocess the dataset for training.
- **Data Transformation**: Transform and preprocess data for model training.
- **Model Training**: Train a text summarization model using the "google/pegasus-cnn_dailymail" model.
- **Logging**: Capture experiment details and errors using the provided logger.

## Getting Started

To run the application, follow these steps:

1. Clone this repository to your local machine:

2. Install the required dependencies:

3. Set up the necessary configurations and ensure that the "sasum dialogue summarization" dataset is accessible.

4. Run the Streamlit application:


5. Access the application in your web browser at the provided URL (usually `http://localhost:8501`).

6. Follow the application steps for data ingestion, validation, transformation, and model training.

## Dataset and Model

- **Dataset**: This application uses the "sasum dialogue summarization" dataset, which should be available and properly configured to run the application.

- **Model**: The text summarization model used in this application is "google/pegasus-cnn_dailymail." Ensure that the model is accessible and properly configured in the code.

## Logging

The application includes logging to capture experiment details and errors. You can find the log files in the "logs" directory. Review these logs for experiment summaries and to troubleshoot any issues that may arise during execution.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them with clear, concise commit messages.
4. Push your branch to your fork: `git push origin feature-name`.
5. Open a pull request, explaining your changes and their purpose.

## Issues and Support

If you encounter any issues or have questions, please feel free to open an issue in the GitHub repository.

Thank you for using the Text Summarization Streamlit Application! I hope it helps you efficiently generate text summaries and gain valuable insights from your data.
