
import paho.mqtt.client as mqtt

TOPIC = "sensor/temperatura/#"

def on_connect(client, userdata, flags, rc):
	print("Conectado com codigo "+str(rc))
	client.subscribe([(TOPIC,0)])

def on_message(client, userdata, msg):
	print msg.topic + "/" + msg.payload.decode()
	#client.disconnect()

client = mqtt.Client()
#client.username_pw_set(username="redes",password="redes")
client.connect("192.168.0.106",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
