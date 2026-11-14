
from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.predictor import predict_messages

app = FastAPI(
    title="SMS Spam Classifier API",
    description="REST API for the RabTech Task 05 TensorFlow SMS spam classifier.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "SMS Spam Classifier API is running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        return {"predictions": predict_messages(request.messages)}
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {exc}")
