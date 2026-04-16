import re
import emoji

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text: str) -> str:
    text = text.lower()
    text = emoji.demojize(text)
    text = re.sub(r"http\S+", "[URL]", text)
    text = re.sub(r"@\w+", "[USER]", text)
    text = re.sub(r"[^a-z\s\[\]!?,.]", "", text)
    return text.strip()


def remove_stopwords(text):
    return " ".join([word for word in text.split() if word not in stop_words])


def lemmatize_text(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])


def apply_full_preprocessing(text):
    processed_text = preprocess(text)
    processed_text = remove_stopwords(processed_text)
    processed_text = lemmatize_text(processed_text)
    return processed_text
