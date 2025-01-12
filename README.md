# Spam Message Detector - README

## Overview
The Spam Message Detector is a machine learning project designed to detect spam messages based on text analysis. The project uses Jupyter Notebook for training the machine learning model and Flask to provide a real-time web interface for spam detection.

## Features
#### * Model Training: Train a machine learning model in Jupyter Notebook to detect spam messages.
#### * Interactive Interface: Flask provides a lightweight and user-friendly interface for classifying messages as spam or not.
#### * Data Visualization: Includes visual insights, such as word clouds, to represent common patterns in spam messages.
#### * Simple Deployment: The Flask app runs locally with a single command.

## Technologies Used
#### 1. Python: Core programming language.
#### 2. Jupyter Notebook: For exploratory data analysis (EDA), model training, and evaluation.
#### 3. Flask: For building the backend and hosting the web interface.

## Libraries:
#### 1. Pandas: Data manipulation and analysis.
#### 2. Scikit-learn: Model training and evaluation.
#### 3. NLTK: For text preprocessing (tokenization, stopword removal).
#### 4. Flask: Web app framework.
#### 5. WordCloud: To visualize the most frequent words in spam messages.

## Project Structure

Spam-Message-Detector

  #### notebooks
     1. model_training.ipynb    # Jupyter notebook for model training and evaluation
  #### static
     2. assets               # Static files such as CSS and images
  #### templates
     3. index.html            # HTML template for the Flask frontend
  4. app.py                    # Flask app script
  5. model.pkl                 # Trained model file (generated after training)
  6. requirements.txt          # List of Python dependencies
  7. README.md                 # Project documentation (this file)

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

1. Open `notebooks/model_training.ipynb` in Jupyter Notebook.
2. Follow the steps in the notebook to:
   * Load the dataset.
   * Preprocess the text data.
   * Train and evaluate the machine learning model.
3. Save the trained model as `model.pkl`.

#### Note: A pre-trained model is already included in the repository.

### 4. Run the Flask App
Run the Flask app with the following command:

    python -m flask run

### 5. Open the App in Your Browser
After running the above command, Flask will start a local server and provide a URL. Open the URL in your browser (default: http://localhost:5000).

## Screenshot
### 1. Login Page
![Screenshot (1)](https://github.com/user-attachments/assets/559433ae-75f7-4510-a850-d874f453ec86)

### 2. Input Page
Here you input the message you want to classify.
![Screenshot (253)](https://github.com/user-attachments/assets/4b7c7a44-bfac-46bc-8d5a-f6c6105649d6)

### 3. Prediction Page
After you enter the message, click the 'Predict' button to classify it as spam or not.
![Screenshot (255)](https://github.com/user-attachments/assets/43da0dd4-fd20-41b7-a5d4-bbff3a1346b1)

### 4. Final Output
The final output will display the result (Spam or Not Spam) along with a word cloud showing frequent words from spam messages.
![Screenshot (257)](https://github.com/user-attachments/assets/13fd912b-b605-472a-b0fd-08d4323f8e6b)

## Additional Features
#### Spam Message Detection: Input a message to check if it is spam or not.
#### Word Cloud Visualization: The app includes a word cloud to visualize the most frequent words found in spam messages.

