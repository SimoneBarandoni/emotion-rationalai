from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

class TextInput(BaseModel):
    text: str

def classify_emotion(text):
    task = "emotion"
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}-latest"
    classifier = pipeline("sentiment-analysis", model=MODEL)
    result = classifier(text)
    return result[0]['label']

@app.post("/predict")
async def predict_emotion(input_data: TextInput):
    """
    Endpoint to predict emotion from input text
    """
    emotion = classify_emotion(input_data.text)
    return {"emotion": emotion}

