# Emotion Detector

Final project for an AI-based web application: an **Emotion Detector** built with Python, the Watson NLP library, and Flask.

## Features

- Detects the emotions **anger, disgust, fear, joy, and sadness** in a piece of text using the Watson NLP EmotionPredict service.
- Returns each emotion's score and the **dominant emotion**.
- Packaged as the `EmotionDetection` Python package.
- Unit tested with `unittest`.
- Deployed as a web application with Flask, with error handling for blank input.
- `server.py` passes static code analysis with PyLint (10/10).

## Run the application

```bash
python3.11 -m pip install flask requests
python3.11 server.py
```

Then open `http://localhost:5000`.

## Run the unit tests

```bash
python3.11 test_emotion_detection.py
```
