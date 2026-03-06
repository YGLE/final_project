import requests  # import requests library

# define emotion_detector function that takes a text input
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the EmotionPredict service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers for the API request
    myobj = {
        "raw document": {
            "text": text_to_analyse
        }
    }  # Create a dictionary with the text in input

    try:
        print(f"Sending POST request to {url}")
        response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API service
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Received response: {response.text}")
        return response.text  # Return the API response
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return f"Error: {e}"