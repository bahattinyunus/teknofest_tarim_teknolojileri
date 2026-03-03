import sys
import os
import numpy as np

# Add src to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from disease_detector import PlantDiseaseDetector
from sensor_node import EnvironmentSensor, NPKSensor

def test_ai_detector():
    detector = PlantDiseaseDetector()
    dummy_img = np.zeros((224, 224, 3))
    
    # Test Apple
    res = detector.detect(dummy_img, crop_type="Apple")
    assert res["crop"] == "Apple"
    assert "condition" in res
    
    # Test unknown crop
    res = detector.detect(dummy_img, crop_type="Unknown")
    assert res["crop"] == "General"

def test_sensors():
    env = EnvironmentSensor("TEST-01", (0, 0))
    data = env.read_data()
    assert data["type"] == "Environment"
    assert "temperature" in data
    
    npk = NPKSensor("TEST-02", (1, 1))
    data = npk.read_data()
    assert data["type"] == "NPK"
    assert "N" in data

if __name__ == "__main__":
    print("Running tests...")
    try:
        test_ai_detector()
        print("AI Detector Test: PASSED")
        test_sensors()
        print("Sensors Test: PASSED")
        print("\nAll tests completed successfully!")
    except AssertionError as e:
        print(f"Test FAILED: {e}")
        sys.exit(1)
