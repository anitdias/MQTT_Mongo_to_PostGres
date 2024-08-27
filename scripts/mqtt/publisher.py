import json

from paho.mqtt import client as mqtt
from scripts.utils.mongo import movie_collection


def on_publish(client, userdata, result):
    print('Message Published!')


client = mqtt.Client()

client.on_publish = on_publish

client.connect('localhost', 1883, 60)

data = movie_collection.find({}, {'_id': 0})
for data in data:
    payload = json.dumps(data)
    client.publish("movie/data", payload)

client.disconnect()
