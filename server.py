from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():

    # Get the JSON data from the request
    data = request.get_json()
    # Get the text from the JSON data
    text = data.get("text")

    # If no text is provided, return an error message
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Use the emotion_detector function to detect the emotions in the text
    emotions = emotion_detector(text)

    # Format the response with the detected emotions
    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    # Return the formatted response as a JSON object
    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    # Run the app on the local machine, on port 5000
    app.run(host='0.0.0.0', port=5000)