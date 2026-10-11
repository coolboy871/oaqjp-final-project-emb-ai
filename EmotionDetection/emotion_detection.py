"""Emotion detection using the Watson NLP EmotionPredict service."""
import json
import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Analyze the text and return the emotion scores and the dominant emotion.

    Returns a dictionary with anger, disgust, fear, joy and sadness scores,
    plus the dominant_emotion. For blank input (status code 400), every
    value is None.
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    # Blank or invalid input: the service responds with status code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert the response text to a dictionary and extract the emotion scores
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    # The dominant emotion is the one with the highest score
    dominant_emotion = max(scores, key=scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
