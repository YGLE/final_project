from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Manage error case
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format and return the response
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

@app.route("/")
def render_index_page():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)   