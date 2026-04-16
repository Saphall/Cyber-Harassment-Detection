import pickle

from flask import jsonify
from .preprocess import apply_full_preprocessing


# Load the model and vectorizer
with open("models/one_vs_rest_logistic_regression_model.pkl", "rb") as f:
    classifier_loaded = pickle.load(f)
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer_loaded = pickle.load(f)


def predict(data):
    # Preprocess the input comment
    cleaned_comment = apply_full_preprocessing(data)
    vectorized_comment = tfidf_vectorizer_loaded.transform([cleaned_comment])

    # Make prediction
    prediction_proba = classifier_loaded.predict_proba(vectorized_comment)
    prediction_binary = classifier_loaded.predict(vectorized_comment)

    # Assuming label_cols is defined somewhere or passed
    # For this example, let's hardcode it as it was in the notebook
    label_cols = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]

    # Format results
    proba_results = {
        label: float(prediction_proba[0][i]) for i, label in enumerate(label_cols)
    }
    binary_results = {
        label: int(prediction_binary[0][i]) for i, label in enumerate(label_cols)
    }

    return jsonify(
        {"binary_predictions": binary_results, "probabilities": proba_results}
    )
