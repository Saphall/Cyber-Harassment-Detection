from flask import Blueprint, render_template, request, jsonify

from .model import predict


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/predict", methods=["POST"])
def make_prediction():
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "No comment_text provided"}), 400

    comment = data.get("comment_text", "")
    result = predict(comment)
    return result


# Test
# curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" \
#      -d '{"comment_text": "You are a horrible idiot!"}'
