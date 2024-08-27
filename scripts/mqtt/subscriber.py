import json

import paho.mqtt.client as mqtt
from sqlalchemy.orm import sessionmaker

from scripts.utils.postgres import engine, MovieCollection

Session = sessionmaker(bind=engine)

session = Session()


# Define the callback for connection


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("movie/data")


# Define the callback for message receipt
def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    data = json.loads(msg.payload.decode())
    new_movie = MovieCollection(name=data['name'], date=data['date'], time=data['time'])
    session.add(new_movie)
    session.commit()


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed with mid: {mid}, granted QoS: {granted_qos}")


# Create an MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

# Connect to the broker
client.connect("localhost", 1883, 60)

# Start the network loop
client.loop_forever()
