# Generated from: mqtt_publisher.ipynb
# Converted at: 2026-06-02T17:26:42.936Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import paho.mqtt.client as mqtt
import random
import time 
import json

broker = "broker.hivemq.com"
port = 1883
topic = "digital_twin/data"

client = mqtt.Client(transport="websockets")

try:
    client.connect("broker.hivemq.com", 8000)
    print("Connected successfully!")
except Exception as e:
    print("Error:", e)