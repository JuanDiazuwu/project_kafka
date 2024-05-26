from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    'weathertopic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

client = MongoClient('localhost', 27017)
db = client.weather_data
collection = db.weather

print("Starting Kafka Consumer...")
for message in consumer:
    weather_data = message.value
    collection.insert_one(weather_data)
    print(f"Stored in MongoDB: {weather_data}")
