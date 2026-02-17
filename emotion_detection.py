import requests # import requests library

# define emotion_detector function that take a test in imput
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # url of the EmotionPredict service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # set the headers for the API request
    myobj = { "raw document": { "text": text_to_analyze } } # create a dictionary with the text in input
    response = requests.post(url, json = myobj, headers=header) # send a POST request to the API service
    return response.text
