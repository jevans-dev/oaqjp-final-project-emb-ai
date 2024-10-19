"""
server.py - Flask web deployment for the Emotion Detection application.
"""

from flask import Flask, request, jsonify
# Make sure emotion_detection is correctly installed or the file is in the same directory
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions from the input text.
    Returns a JSON response with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.json.get("text", "")

    if not text_to_analyze:
        return jsonify({
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }), 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    return jsonify({
        'anger': result['anger'], 
        'disgust': result['disgust'], 
        'fear': result['fear'], 
        'joy': result['joy'], 
        'sadness': result['sadness'], 
        'dominant_emotion': result['dominant_emotion']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
