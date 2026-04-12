from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Wine Quality Prediction API",
    description="Inference API for predicting wine quality using trained Random Forest ML model",
    version="1.0"
)

# -----------------------------
# Load trained model bundle
# -----------------------------
bundle = joblib.load("outputs/model.joblib")

model = bundle["model"]
scaler = bundle["scaler"]
selector = bundle["selector"]


# -----------------------------
# Pydantic Model (JSON Body)
# -----------------------------
class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def read_root():
    return {"message": "Wine Quality Prediction API is running"}


# -----------------------------
# Health Endpoint
# -----------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict_wine_quality(data: WineInput):
    try:
        # Convert input to numpy array
        features = np.array([[  
            data.fixed_acidity,
            data.volatile_acidity,
            data.citric_acid,
            data.residual_sugar,
            data.chlorides,
            data.free_sulfur_dioxide,
            data.total_sulfur_dioxide,
            data.density,
            data.pH,
            data.sulphates,
            data.alcohol
        ]])

        # Apply SAME preprocessing as training
        features_scaled = scaler.transform(features)
        features_selected = selector.transform(features_scaled)

        # Prediction
        prediction = model.predict(features_selected)

        return {
            "name": "Karri Lakshmi Narasimha Reddy",
            "roll_no": "2022BCS0028",
            "prediction": int(prediction[0])
        }

    except Exception as e:
        return {"error": str(e)}