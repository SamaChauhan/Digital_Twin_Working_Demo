# Generated from: simulator.ipynb
# Converted at: 2026-06-02T17:26:09.894Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import random
import time
import json

def generate_data():
    
    data = {
        "Temperature: ": round(random.uniform(22,30), 2),
        "Occupancy: ": random.choice([0,1]),
        "Power: ": round(random.uniform(100,500), 2)
    }
    return data

while True:
    sensor_data = generate_data()
    print(sensor_data)
    time.sleep(2)