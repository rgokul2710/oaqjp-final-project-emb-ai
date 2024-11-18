import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {"raw_document" : {"text" : text_to_analyse }}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()['emotionPredictions'][0]['emotion']
        dominant_emotion = max(result, key=result.get)
        result['dominant_emotion'] = dominant_emotion
        print(result)
    else:
        print(f"Error {response.status_code}: {response.text}")