# RabTech Task 06 – Real-Time ML Inference REST API & Capstone

## Project overview
This project exposes the SMS Spam Classification model developed in Task 05 through a REST API built with FastAPI. The API accepts SMS text as JSON and returns a predicted class with spam/ham probabilities.

## Architecture
1. Client sends SMS text to `POST /predict`.
2. FastAPI validates the JSON payload with Pydantic.
3. The prediction module loads the saved Keras model on the first prediction and reuses it.
4. The model returns a spam score; the API converts it into `spam` or `ham` and complementary probabilities.
5. The API returns structured JSON.

## Project structure
```text
RabTech_Task06_Capstone/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── predictor.py
│   └── schemas.py
├── models/
│   └── sms_spam_classifier.keras
├── tests/
│   └── test_api.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Required model file
Copy your Task 05 model into `models/` and rename it exactly:
`sms_spam_classifier.keras`

Expected source filename: `RabTech_Task05_SMS_Spam_Classifier.keras`.

The model file is not included in this package because it must be the actual model trained in your Task 05 notebook. This code expects the Keras model to accept raw SMS strings and return one sigmoid spam probability per message (with text vectorization included in the saved model).

## Run locally (Windows)
```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs` for interactive API documentation.

## API endpoints
- `GET /` – API status.
- `GET /health` – basic health response.
- `POST /predict` – classifies one or more SMS messages.

Request:
```json
{"messages": ["You won a free prize!", "Are we still meeting at 6?"]}
```

Example response (illustrative only; actual scores depend on your trained model):
```json
{
  "predictions": [
    {
      "message": "You won a free prize!",
      "label": "spam",
      "spam_probability": 0.91,
      "ham_probability": 0.09
    }
  ]
}
```
The example scores are placeholders, not measured results. If the model file is missing, `/predict` returns HTTP 503.

## Run tests
```bash
pytest -q
```
Tests mock prediction, so API request validation and response handling can be tested without the trained model.

## Docker
Ensure `models/sms_spam_classifier.keras` exists, then:
```bash
docker build -t rabtech-sms-api .
docker run --rm -p 8000:8000 rabtech-sms-api
```
Visit `http://localhost:8000/docs`.

## Notes
This is an educational project, not a production-grade service. SMS classification can make mistakes; do not use it as the sole basis for important decisions.
