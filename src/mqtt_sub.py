import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()}")

client = mqtt.Client()
client.username_pw_set("dashboard", "matkhau_dashboard")
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("iot/sensor/temp")
client.loop_forever()
