import requests  # import requests library
import json # import json library

# define emotion_detector function that takes a text input
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the EmotionPredict service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers for the API request
    payload = {"raw_document": {"text": text_to_analyze}}  # Create a dictionary with the text in input

    try:
        #print(f"Sending POST request to {url}")
        response = requests.post(url, json = payload, headers=headers)  # Send a POST request to the API service
        response.raise_for_status()  # Raise an exception for HTTP errors
        #print(f"Received response: {response.text}")
        #return response.text  # return the API response
        response_dict = json.loads(response.text) # convert response to a dictionary

        # extract scores of emotion
        emotion_data = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']
        
        # find the dominant emotion
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(scores, key=scores.get)

        # return the dominant emotion
        return {
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
            print("Error 400 : Empty text or bad format")
        elif response.status_code == 403:
            print("Error 403 : Access denied - Check header grpc-metadata-mm-model-id")
        elif response.status_code == 500:
            print("Error 500 : Server issue  - Please check later")
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}") 
    return {
        'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,
        'dominant_emotion': None
        }