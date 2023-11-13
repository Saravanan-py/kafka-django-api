import json
from kafka import KafkaConsumer


# def consumer(category):
#     topic = 'employee'
#     consumer = KafkaConsumer(
#         bootstrap_servers=["localhost:9092", 'localhost:9093', 'localhost:9094'],
#         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
#         auto_offset_reset="earliest"
#     )
#     consumer.subscribe(topic)
#     print("Waiting for location details.....")
#     while True:
#         if consumer:
#             print("*" * 50)
#             for message in consumer:
#                 if message.value['Category'] == category:
#                     category = message.value['Category']
#                     link = message.value['Link']
#                     data = {'Category': category, 'Link': link}
#                     print(data)
def consumer():
    consumer = KafkaConsumer('url-sample', bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             auto_offset_reset = "earliest"
                             )
    for message in consumer:
        print(message.value)
