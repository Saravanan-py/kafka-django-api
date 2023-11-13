from kafka.producer import KafkaProducer
from time import sleep
import json
from .models import collection
from json import dumps
# import requests


#
# def employee():
#     topic = 'employee'
#     producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
#                              value_serializer=lambda x: dumps(x).encode('utf-8'))
#     response_API = requests.get('https://api.publicapis.org/entries')
#     data = response_API.text
#     parse_json = json.loads(data)
#     for i in range(len(parse_json['entries'])):
#         data = parse_json['entries'][i]
#         producer.send(topic, value=data)
#         sleep(1)

def producer():

    # Kafka topic to produce to
    kafka_topic = 'url-sample'

    # URL to include in the data
    url = 'http://65.1.111.158:5000/produce?data='

    # Create a Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    with open(r"C:\Users\Vrdella\Downloads\MOCK_DATA.json", 'r') as f:
        data = json.load(f)
    for i in range(len(data)):
        data[i].update({"ID": "VIV" + str(i)})
        data_to_produce = {
            'url': url,
            'other_data_field': data[i]
        }
        producer.send(kafka_topic, value=data_to_produce)
        collection.insert_one(data[i])
        sleep(2)
