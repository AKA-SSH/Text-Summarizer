import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# !python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    doc = nlp(text)
    
    processed_tokens = []
    for token in doc:
        if token.ent_type_ in ('PERSON', 'ORG', 'GPE', 'LOC'):
            processed_tokens.append(token.text)
        else:
            processed_tokens.append(token.text.lower())

    text = ' '.join(processed_tokens)
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    preprocessed_text = ' '.join(words)
    
    return preprocessed_text