"""
Test Suite for Sensor Node Module
"""

import pytest
from src.sensor_node import SensorNode, NPKSensor, MoistureSensor


def test_sensor_node_initialization():
    """Test basic sensor node creation"""
    sensor = NPKSensor(node_id="NPK-001", location=(40.5, 41.0))
    assert sensor.node_id == "NPK-001"
    assert sensor.location == (40.5, 41.0)


def test_npk_sensor_read_data():
    """Test NPK sensor data reading"""
    sensor = NPKSensor(node_id="NPK-001", location=(40.5, 41.0))
    data = sensor.read_data()
    assert "N" in data
    assert "P" in data
    assert "K" in data


def test_moisture_sensor_read_data():
    """Test moisture sensor data reading"""
    sensor = MoistureSensor(node_id="MOIST-001", location=(40.5, 41.0))
    data = sensor.read_data()
    assert "moisture" in data
    assert isinstance(data["moisture"], float)
