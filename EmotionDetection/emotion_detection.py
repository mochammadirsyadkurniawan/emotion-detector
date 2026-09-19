"""Emotion detection using the Watson NLP service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse):
    """Analyze the emotion of the supplied text."""

    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if text_to_analyse is None or not text_to_analyse.strip():
        return empty_result

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json=input_json,
            timeout=60
        )
    except requests.RequestException:
        return empty_result

    if response.status_code == 400:
        return empty_result

    response.raise_for_status()

    formatted_response = response.json()

    predictions = formatted_response.get("emotionPredictions", [])

    if not predictions:
        return empty_result

    emotions = predictions[0].get("emotion", {})

    emotion_scores = {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness")
    }

    valid_scores = {
        key: value
        for key, value in emotion_scores.items()
        if value is not None
    }

    if not valid_scores:
        return empty_result

    dominant_emotion = max(
        valid_scores,
        key=valid_scores.get
    )

    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores