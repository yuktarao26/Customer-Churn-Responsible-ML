
from pydantic import BaseModel, Field
from typing import List


class PredictRequest(BaseModel):
    messages: List[str] = Field(..., min_length=1)


class PredictionItem(BaseModel):
    message: str
    label: str
    spam_probability: float = Field(..., ge=0.0, le=1.0)
    ham_probability: float = Field(..., ge=0.0, le=1.0)


class PredictResponse(BaseModel):
    predictions: List[PredictionItem]
