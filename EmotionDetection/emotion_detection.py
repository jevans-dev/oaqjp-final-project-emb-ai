import requests
import json

def emotion_detector(text_to_analyze):
    
    # Define the URL for the Watson emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Define the headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    
    # Define the input data for the request
    input_data = {"raw_document": {"text": text_to_analyze}}
    
    
    # Send a POST request to the Watson emotion prediction service
    response = requests.post(url, headers=headers, json=input_data)
    
    
    # Load the response as a dictionary
    response_dict = json.loads(response.text)
    
    
    # Extract the emotion predictions from the response
    emotions = response_dict.get('emotion_predictions', [{}])[0]
    # Extract the anger score from the emotion predictions
    anger = emotions.get('anger', 0)
    # Extract the disgust score from the emotion predictions
    disgust = emotions.get('disgust', 0)
    # Extract the fear score from the emotion predictions
    fear = emotions.get('fear', 0)
    # Extract the joy score from the emotion predictions
    joy = emotions.get('joy', 0)
    # Extract the sadness score from the emotion predictions
    sadness = emotions.get('sadness', 0)
    
    
    # Create a dictionary of emotion scores
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    # Determine the dominant emotion based on the emotion scores
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    
    # Return a dictionary containing the emotion scores and the dominant emotion
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }


if __name__ == "__main__":
    # Call the emotion_detector function with a sample text
    result = emotion_detector("I am so happy I am doing this.")
    # Print the result
    print(result)