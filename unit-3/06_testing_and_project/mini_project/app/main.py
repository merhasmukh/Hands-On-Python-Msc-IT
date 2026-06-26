from fastapi import FastAPI
from pydantic import BaseModel
from .model import fake_model  # Import from local model.py

app = FastAPI(title="AI Sentiment Analysis API")

# Input Schema
class TextRequest(BaseModel):
    text: str

# Output Schema
class PredictionResponse(BaseModel):
    sentiment: str

@app.get("/")
def read_root():
    return {"message": "AI Model API is running. Send POST requests to /predict"}

@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(req: TextRequest):
    # Call the model
    result = fake_model.predict(req.text)
    return PredictionResponse(sentiment=result)

# Run with: uvicorn app.main:app --reload
