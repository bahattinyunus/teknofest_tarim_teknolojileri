import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import random
import numpy as np

# Add src to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from disease_detector import PlantDiseaseDetector
from sensor_node import EnvironmentSensor, NPKSensor, MoistureSensor

app = FastAPI(
    title="Agri-Arch-TR API",
    description="Advanced Backend API for Smart Agriculture System",
    version="1.1.0"
)

# Initialize Core Modules
detector = PlantDiseaseDetector()

class PredictionRequest(BaseModel):
    image_id: str
    crop_type: Optional[str] = "Apple"

class SensorResponse(BaseModel):
    data: List[Dict[str, Any]]

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Agri-Arch-TR Command Center API",
        "version": "1.1.0",
        "status": "operational"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "agri-backend"}

@app.get("/sensors", response_model=SensorResponse)
def get_sensor_data():
    """Fetch live data from simulated LoRaWAN nodes"""
    nodes = [
        EnvironmentSensor("ENV-01", (38.4, 27.1)),
        NPKSensor("NPK-01", (38.42, 27.15)),
        MoistureSensor("MOIST-01", (38.39, 27.12))
    ]
    
    results = [node.read_data() for node in nodes]
    for node in nodes:
        node.transmit()
        
    return {"data": results}

@app.post("/predict")
def predict_disease(request: PredictionRequest):
    """AI disease detection based on project logic"""
    # Simulate an image array
    dummy_img = np.zeros((224, 224, 3)) 
    
    result = detector.detect(dummy_img, crop_type=request.crop_type)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
        
    return result
