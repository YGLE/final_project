import requests  # import requests library
#import json # import json library

text_to_analyse = "I love this new technology"

# define emotion_detector function that takes a text input
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the EmotionPredict service
    headers = {
        "accept": "application/json", 
        "content-type": "application/json", 
        "Grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }  # Set the headers for the API request
    myobj = {
        "raw document": {
            "text": text_to_analyse
        }, 
        "target_phrases": ["bananas"]
    }  # Create a dictionary with the text in input

    try:
        print(f"Sending POST request to {url}")
        response = requests.post(url, json = myobj, headers=headers)  # Send a POST request to the API service
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Received response: {response.text}")
        return response.text  # Return the API response
    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
            print("Erreur : Texte vide ou mal formaté")
        elif response.status_code == 403:
            print("Erreur : Accès refusé - Vérifiez l'en-tête grpc-metadata-mm-model-id")
        elif response.status_code == 500:
            print("Erreur serveur temporaire - Réessayez plus tard")
        else:
            print(f"Erreur HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}") 