"""
IoT Module - LoRaWAN Sensor Integration

This module handles communication with agricultural sensors using LoRaWAN protocol.
"""

import random
import time
from datetime import datetime
from typing import Dict, Any


class SensorNode:
    """Base class for sensor nodes in the field"""
    
    def __init__(self, node_id: str, location: tuple):
        self.node_id = node_id
        self.location = location  # (lat, lon)
        
    def _get_base_data(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "timestamp": datetime.now().isoformat(),
            "location": self.location,
            "signal_strength": random.randint(-120, -30) # dBm
        }

    def read_data(self):
        """Read sensor data from the node"""
        raise NotImplementedError
        
    def transmit(self) -> bool:
        """Transmit data via LoRaWAN"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Node {self.node_id} transmitting payload...")
        time.sleep(0.1)  # Simulate network latency
        return True


class EnvironmentSensor(SensorNode):
    """Ambient Temperature and Humidity Sensor"""
    
    def read_data(self) -> Dict[str, Any]:
        data = self._get_base_data()
        data.update({
            "type": "Environment",
            "temperature": round(random.uniform(15.0, 35.0), 2),
            "humidity": round(random.uniform(30.0, 80.0), 2),
            "unit": {"temp": "C", "hum": "%"}
        })
        return data


class NPKSensor(SensorNode):
    """NPK (Nitrogen, Phosphorus, Potassium) Soil Sensor"""
    
    def read_data(self) -> Dict[str, Any]:
        data = self._get_base_data()
        data.update({
            "type": "NPK",
            "N": random.randint(20, 100),
            "P": random.randint(10, 50),
            "K": random.randint(100, 300),
            "unit": "mg/kg"
        })
        return data


class MoistureSensor(SensorNode):
    """Soil Moisture Sensor"""
    
    def read_data(self) -> Dict[str, Any]:
        data = self._get_base_data()
        data.update({
            "type": "Moisture",
            "moisture": round(random.uniform(10.0, 90.0), 2),
            "unit": "%"
        })
        return data


class GPSGateway(SensorNode):
    """Gateway node that coordinates field data and mobile position"""
    
    def __init__(self, node_id: str, location: tuple):
        super().__init__(node_id, location)
        self.active_nodes = []

    def sync_nodes(self, nodes: list):
        self.active_nodes = [n.node_id for n in nodes]
        print(f"Gateway {self.node_id} synced with {len(self.active_nodes)} nodes.")

