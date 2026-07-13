import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.username_pw_set("sensor", "matkhau_sensor") 
client.connect("localhost", 1883, 60)

data = {"temperature": 25.5}
client.publish("iot/sensor/temp", json.dumps(data))
print("Sent: Đã gửi dữ liệu thành công")
client.disconnect()
