from kafka.producer import KafkaProducer
from time import sleep
import json
from json import dumps
import requests


def employee():
    topic = 'employee'
    producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    response_API = requests.get('https://api.publicapis.org/entries')
    data = response_API.text
    parse_json = json.loads(data)
    for i in range(len(parse_json['entries'])):
        data = parse_json['entries'][i]
        producer.send(topic, value=data)
        sleep(1)
