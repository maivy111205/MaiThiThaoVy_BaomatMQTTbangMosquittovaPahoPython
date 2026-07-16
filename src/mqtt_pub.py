import json
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/temp"

USERNAME = "sensor"
PASSWORD = "YOUR_PASSWORD"

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

try:
    client.connect(BROKER, PORT, 60)

    payload = {
        "device": "sensor01",
        "temperature": 30,
        "humidity": 70,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    client.publish(TOPIC, json.dumps(payload))

    print("===================================")
    print("Publisher")
    print("Connected to Broker")
    print("Topic:", TOPIC)
    print("Payload:")
    print(json.dumps(payload, indent=4))
    print("Publish Success")
    print("===================================")

    client.disconnect()

except Exception as e:
    print("Connection Error:", e)
