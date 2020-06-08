from app import mqttc
from app.mqtt.functions import on_message, on_disconnect, on_connect, on_log
from config import Config

mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_log = on_log
mqttc.on_message = on_message

mqttc.connect(Config.MQTT_BROKER_URL)

mqttc.subscribe("house/sensor1")
mqttc.publish("house/sensor1", "my first message")

mqttc.loop_forever()
