# Spam Message Detector - README

## Overview
The Spam Message Detector is a machine learning project designed to classify messages as spam or not spam. This project uses Jupyter Notebook for training the model and Streamlit for building an interactive web-based frontend for real-time predictions.

## Features
#### Model Training: Train a machine learning model in Jupyter Notebook to classify text messages.
#### Interactive Interface: Streamlit is used to create a user-friendly interface for predicting whether a message is spam or not.
#### Simple Deployment: Run the app locally using Streamlit with a single command.

## Technologies Used
#### 1.Python: Core programming language.
#### 2.Jupyter Notebook: For exploratory data analysis (EDA), model training, and evaluation.
#### 3.Streamlit: For building an intuitive web-based frontend.

## Libraries:
#### 1.Pandas: Data manipulation and analysis.
#### 2.Scikit-learn: Model training and evaluation.
#### 3.NLTK/Spacy: For text preprocessing (if applicable).
#### 4.Streamlit: Web app framework.

## Project Structure

Spam-Message-Detector
 
 #### notebooks
     1.model_training.ipynb  -> Jupyter notebook for model training and evaluation
     2.app.py                  -> Streamlit app script
     3.model.pkl               -> Trained model file (generated after training)
     4.requirements.txt        -> List of Python dependencies
     5.README.md               -> Project documentation (this file)

## How to Run the Project
### 1. Clone the Repository
Clone the repository to your local machine:

    git clone <repository-url>
    cd Spam-Message-Detector

### 2. Install Dependencies
Install the required Python libraries:

    pip install -r requirements.txt

### 3. Train the Model
If you'd like to retrain the model:

    1. Open notebooks/model_training.ipynb in Jupyter Notebook.
    2. Follow the steps in the notebook to:
        * Load the dataset.
        * Preprocess the text data.
        * Train and evaluate the machine learning model.
    3. Save the trained model as model.pkl.

#### Note: A pre-trained model is already included in the repository.

### 4. Run the Streamlit App
Run the Streamlit app with the following command:

    streamlit run app.py

### 5. Open the App in Your Browser
After running the above command, Streamlit will start a local server and provide a URL. Open the URL in your browser (default: http://localhost:8501).

## Using the App
  #### * Input a Message: Enter the text message you want to classify in the input box.
  #### * Get Prediction: Click the "Classify" button to see whether the message is spam or not spam.
  #### * Real-Time Updates: Make changes or test multiple messages seamlessly.

## Customization
 #### * Modify the app.py file to customize the Streamlit interface.
 #### * Use the notebooks/model_training.ipynb file to experiment with different models or datasets.

## Example Workflow
 #### * Train the model in Jupyter Notebook using a dataset of labeled spam and non-spam messages.
 #### * Save the trained model to a .pkl file.
 #### * Use Streamlit to load the model and provide a real-time interface for predictions.

## Command Reference
 #### 1.Run the app:   
    streamlit run app.py
 #### 2.Install dependencies:
    pip install -r requirements.txt

## Contributing
   Feel free to submit issues or pull requests to improve the project!

