from pydantic import BaseModel

class AIModel:
    def __init__(self):
        # In a real scenario, this would load weights from a .pt or .pkl file.
        print("Model Loaded!")

    def predict(self, text: str) -> str:
        # Mock logic
        text_lower = text.lower()
        if "bad" in text_lower or "sad" in text_lower or "terrible" in text_lower:
            return "Negative"
        elif "good" in text_lower or "happy" in text_lower or "great" in text_lower:
            return "Positive"
        else:
            return "Neutral"

# Instantiate the model once
fake_model = AIModel()
