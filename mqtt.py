import contextlib
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

pub_topic = "directions"
mqttc = mqtt.Client()

class Mqtt():
    def client(self):
        print("test")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(self, client, userdata, msg):
        message = str(msg.payload)
        print(msg.topic+" "+message)

    def publish(self, msg):
        mqttc.publish(pub_topic, msg)

    def on_publish(self, mosq, obj, mid):
        print("mid: " + str(mid))

    mqttc.username_pw_set("user", "pw")
    mqttc.connect("m11.cloudmqtt.com", 13590)
    mqttc.publish(pub_topic, "connecting")