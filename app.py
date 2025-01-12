from flask import Flask, render_template, request
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the PorterStemmer
ps = PorterStemmer()

# Load the pre-trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Function to preprocess the input text
def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = nltk.word_tokenize(text)  # Tokenize the text into words

    y = []
    for i in text:
        if i.isalnum():  # Remove special characters
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)  # Remove stopwords and punctuation

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))  # Apply stemming

    return " ".join(y)

# Define route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        input_sms = request.form['sms']
        transform_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transform_sms])
        prediction = model.predict(vector_input)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
    return render_template("home.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
