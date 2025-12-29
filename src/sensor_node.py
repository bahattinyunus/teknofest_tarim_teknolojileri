"""
IoT Module - LoRaWAN Sensor Integration

This module handles communication with agricultural sensors using LoRaWAN protocol.
"""


import random

class SensorNode:
    """Base class for sensor nodes in the field"""
    
    def __init__(self, node_id: str, location: tuple):
        self.node_id = node_id
        self.location = location
        
    def read_data(self):
        """Read sensor data from the node"""
        raise NotImplementedError
        
    def transmit(self):
        """Transmit data via LoRaWAN"""
        print(f"Node {self.node_id} transmitting data...")
        return True


class NPKSensor(SensorNode):
    """NPK (Nitrogen, Phosphorus, Potassium) Soil Sensor"""
    
    def read_data(self):
        """Simulate NPK reading"""
        return {
            "N": random.randint(20, 100),  # mg/kg
            "P": random.randint(10, 50),
            "K": random.randint(100, 300)
        }


class MoistureSensor(SensorNode):
    """Soil Moisture Sensor"""
    
    def read_data(self):
        """Simulate moisture reading"""
        return {"moisture": round(random.uniform(10.0, 90.0), 2)}

