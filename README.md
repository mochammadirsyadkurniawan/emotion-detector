# Emotion Detector

## Project Description

Emotion Detector is a web-based application that analyzes a text statement and identifies the emotions expressed in the statement.

The application uses Watson NLP for emotion detection and Flask as the web application framework.

## Detected Emotions

The application detects five emotions:

- Anger
- Disgust
- Fear
- Joy
- Sadness

The application also determines the dominant emotion based on the highest emotion score.

## Technologies Used

- Python 3
- Flask
- Requests
- Watson NLP
- unittest
- Pylint
- HTML
- CSS

## Project Structure

```text
emotion-detector/
├── .gitignore
├── README.md
├── requirements.txt
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
└── templates/
    └── index.html