import requests
import json

# Define a function to detect emotions from a given text
def emotion_detector(text_to_analyze):

    # Check if the text to analyze is empty or None
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return a dictionary with all emotions set to None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL and headers for the API request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the input data for the API request
    input_data = {"raw_document": {"text": text_to_analyze}}

    # Make the API request
    response = requests.post(url, headers=headers, json=input_data)

    # Check if the API request was successful
    if response.status_code == 400:
        # Return a dictionary with all emotions set to None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response from the API
    response_dict = json.loads(response.text)

    # Extract the emotion predictions from the response
    emotions = response_dict.get('emotion_predictions', [{}])[0]
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)

    # Create a dictionary with the emotion scores
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return a dictionary with the emotion scores and the dominant emotion
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

