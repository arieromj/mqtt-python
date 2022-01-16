
import paho.mqtt.client as mqtt
from random import randint
from time import sleep

TOPIC = "sensor/temperatura"

client = mqtt.Client()
#client.username_pw_set(username="redes",password="redes")
client.connect("192.168.0.106",1883,60)

while True:
	t = randint(0, 50)
	client.publish(TOPIC, t);
	print "Dado " + str(t) + " publicado no topico: %s" % (TOPIC)
	
	sleep(5)



#client.disconnect();

