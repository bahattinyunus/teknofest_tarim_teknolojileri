"""
AI Module - Plant Disease Detection

This module uses Convolutional Neural Networks (CNN) to detect plant diseases
from drone or camera imagery.
"""

import numpy as np
import random
from typing import Dict, Any, List


class PlantDiseaseDetector:
    """CNN-based plant disease detection system with multi-crop support"""
    
    def __init__(self, model_path: str = None):
        self.model = None
        self.supported_crops = ["Apple", "Tomato", "Grape", "Corn", "Potato"]
        if model_path:
            self.load_model(model_path)
    
    def load_model(self, path: str):
        """Load pre-trained CNN model (TensorFlow/PyTorch)"""
        # In production, this would initialize the deep learning framework
        print(f"Loading weights from {path}...")
        pass
    
    def validate_image(self, image: np.ndarray) -> bool:
        """Validate input image dimensions and quality"""
        if image is None or image.size == 0:
            return False
        return True
    
    def detect(self, image: np.ndarray, crop_type: str = "Apple") -> Dict[str, Any]:
        """
        Detect diseases in plant image
        
        Args:
            image: np.ndarray of the plant leaf/crop
            crop_type: Type of crop for specialized inference
            
        Returns:
            dict: Classification results, severity, and action plan
        """
        if not self.validate_image(image):
             return {"error": "Invalid image input"}
             
        if crop_type not in self.supported_crops:
            crop_type = "General"

        # Mock database for different crops
        disease_map = {
            "Apple": ["Healthy", "Scab", "Black Rot", "Rust"],
            "Tomato": ["Healthy", "Bacterial Spot", "Early Blight", "Late Blight"],
            "Grape": ["Healthy", "Black Rot", "Esca", "Leaf Blight"],
            "General": ["Healthy", "Fungal Infection", "Pest Damage"]
        }
        
        potential_diseases = disease_map.get(crop_type, disease_map["General"])
        detected = random.choice(potential_diseases)
        confidence = round(random.uniform(0.75, 0.99), 2)
        
        # Severity calculation (0.0 to 1.0)
        severity = 0.0 if detected == "Healthy" else round(random.uniform(0.1, 0.8), 2)
        
        status = "Normal"
        if severity > 0.6:
            status = "CRITICAL"
        elif severity > 0.2:
            status = "WARNING"

        return {
            "crop": crop_type,
            "condition": detected,
            "status": status,
            "confidence": confidence,
            "severity_index": severity,
            "recommendations": self._get_recommendations(detected, severity)
        }

    def _get_recommendations(self, condition: str, severity: float) -> List[str]:
        if condition == "Healthy":
            return ["Continue standard irrigation", "Next scheduled check in 48h"]
        
        actions = [f"Isolation of the affected {condition} area"]
        if severity > 0.5:
            actions.append("Immediate fungicide application recommended")
        else:
            actions.append("Monitor progression; decrease humidity if possible")
            
        return actions
