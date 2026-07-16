import os
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/temp"

USERNAME = "dashboard"
PASSWORD = "MAT_KHAU_THU_NGHIEM"

LOG_FILE = "../results/logs/mqtt_log.txt"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Broker")
        client.subscribe(TOPIC)
    else:
        print("Connection Failed")

def on_message(client, userdata, msg):
    message = msg.payload.decode()

    print("\n==============================")
    print("Message Received")
    print("Topic:", msg.topic)
    print("Payload:", message)
    print("==============================")

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{msg.topic} : {message}\n")

client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()
