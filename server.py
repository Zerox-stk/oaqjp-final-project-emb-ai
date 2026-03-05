from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_api():

    text_to_analyze = (
        request.args.get("textToAnalyze")
        or request.args.get("text")
        or request.form.get("textToAnalyze")
        or request.form.get("text")
        or (request.json.get("text") if request.is_json and request.json else None)
    )

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
