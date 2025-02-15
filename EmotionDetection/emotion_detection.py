import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    emotions_dict = {}
    dominant = ""
    if response.status_code == 200:
        emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
        for emotion in emotions:
            emotions_dict[emotion] = emotions[emotion]
            if dominant == "":
                dominant = emotion
                score = float(emotions[emotion])
            elif float(emotions[emotion]) > score:
                dominant = emotion
                score = float(emotions[emotion])
            emotions_dict['dominant_emotion'] = dominant
    elif response.status_code == 400:
        emotions_dict['anger'] = None
        emotions_dict['disgust'] = None
        emotions_dict['fear'] = None
        emotions_dict['joy'] = None
        emotions_dict['sadness'] = None
        emotions_dict['dominant_emotion'] = None
    return emotions_dict
