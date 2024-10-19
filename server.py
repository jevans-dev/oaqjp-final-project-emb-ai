from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

# Create a Flask application
app = Flask(__name__)

# Define a route for the emotion detector
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():

    # Get the data from the request
    data = request.get_json()
    text = data.get("text")

    # Check if the text is valid
    if not text:
        return jsonify({"response": "Invalid text! Please try again."}), 400

    # Use the emotion_detector function to detect the emotions
    emotions = emotion_detector(text)

    # Check if the dominant emotion is valid
    if emotions['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again."}), 400

    # Format the response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    # Return the response
    return jsonify({"response": formatted_response})

# Run the Flask application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

