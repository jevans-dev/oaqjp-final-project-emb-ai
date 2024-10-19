import requests

# Define a function to detect emotions from a given text
def emotion_detector(text_to_analyze):
    
    # Set the URL for the API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    
    # Set the input data for the API
    input_data = {"raw_document": {"text": text_to_analyze}}
    
    
    # Send a POST request to the API with the input data and headers
    response = requests.post(url, headers=headers, json=input_data)
    
    
    # Return the response from the API
    return response.text


# If the script is run directly, call the emotion_detector function with a sample text and print the result
if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(result)
