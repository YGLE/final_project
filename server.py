from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Récupérer le texte depuis les paramètres de la requête
    text_to_analyze = request.args.get('textToAnalyze')

    # Appeler la fonction emotion_detector
    result = emotion_detector(text_to_analyze)

    # Gérer le cas de texte vide ou None
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Formater la réponse comme demandé
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