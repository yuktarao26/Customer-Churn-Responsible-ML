
from pathlib import Path
import numpy as np
from tensorflow import keras

MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "sms_spam_classifier.keras"
)

_model = None


def get_model():
    global _model

    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model not found at {MODEL_PATH}"
            )

        _model = keras.models.load_model(MODEL_PATH)

    return _model


def predict_messages(messages):
    model = get_model()

    scores = np.asarray(
        model.predict(np.asarray(messages, dtype=str), verbose=0)
    ).reshape(-1)

    results = []

    for message, score in zip(messages, scores):
        spam_probability = float(np.clip(score, 0.0, 1.0))

        results.append({
            "message": message,
            "label": "spam" if spam_probability >= 0.5 else "ham",
            "spam_probability": spam_probability,
            "ham_probability": 1.0 - spam_probability,
        })

    return results
