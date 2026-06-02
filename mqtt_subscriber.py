
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "digital_twin/data"

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client(transport="websockets")
client.connect("broker.hivemq.com", 8000)

client.subscribe(topic)
client.on_message = on_message

client.loop_forever()
