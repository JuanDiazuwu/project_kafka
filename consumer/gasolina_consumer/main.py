from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    'gasolinatopic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='gasolina-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

client = MongoClient('localhost', 27017)
db = client.gasolina_data
collection = db.gasolina

print("Starting Kafka Consumer...")
for message in consumer:
    gasolina_data = message.value
    gasolina_data_dict = json.loads(gasolina_data)
    #gasolina_data_dict = dict(gasolina_data)
    collection.insert_one(gasolina_data_dict)
    print(f"Stored in MongoDB: {gasolina_data}")
