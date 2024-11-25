import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt_tab')

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()  ## this method change uppercase Into lowercase
    text = nltk.word_tokenize(text)  ## this method convert text into single words

    y = []
    for i in text:
        if i.isalnum():  ## is alpha numeric   # Removing special character
            y.append(i)

    text = y[:]  ## here we empty our list
    y.clear()  ## clear the y

    for i in text:
        if i not in stopwords.words(
                'english') and i not in string.punctuation:  ## here we checking Stopwords and punctuation means all symbol,maths,brackets,quotation ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
            y.append(i)  ## return fresh Y

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))  ##Steaming words into small words like running -> run

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/sms Spam Classifier')
st.text('By Priyanshu')

input_sms = st.text_area("enter the message")
if st.button('Predict'):
    # 1.Preprocess
    transform_sms = transform_text(input_sms)
    # 2.vectorize
    vector_input = tfidf.transform([transform_sms])
    # 3.predict
    result = model.predict(vector_input)[0]
    # 4.display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

# For Running this code:
#     streamlit run app.py

