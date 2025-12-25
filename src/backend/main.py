from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI(
    title="Agri-Arch-TR API",
    description="Backend API for Smart Agriculture System",
    version="1.0.0"
)

class SensorData(BaseModel):
    node_id: str
    sensor_type: str
    value: float
    unit: str

class DiseasePrediction(BaseModel):
    plant_id: str
    disease: str
    confidence: float
    treatment: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Agri-Arch-TR Command Center API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "agri-backend"}

@app.get("/sensors", response_model=List[SensorData])
def get_sensor_data():
    """Simulate fetching data from LoRaWAN gateway"""
    mock_data = [
        SensorData(node_id="NODE-01", sensor_type="Moisture", value=random.uniform(30.0, 60.0), unit="%"),
        SensorData(node_id="NODE-01", sensor_type="Nitrogen", value=random.uniform(10.0, 50.0), unit="mg/kg"),
        SensorData(node_id="NODE-02", sensor_type="Temperature", value=random.uniform(15.0, 30.0), unit="C"),
    ]
    return mock_data

@app.post("/predict", response_model=DiseasePrediction)
def predict_disease(image_id: str):
    """Simulate AI disease detection"""
    # In a real app, this would use the CNN model
    diseases = ["Early Blight", "Late Blight", "Healthy", "Rust"]
    detected = random.choice(diseases)
    
    return DiseasePrediction(
        plant_id=image_id,
        disease=detected,
        confidence=random.uniform(0.85, 0.99),
        treatment="Apply fungicide X if severety > 0.5" if detected != "Healthy" else "None"
    )
