import matplotlib.pyplot as plt
from pymongo import MongoClient
import datetime

# Conexión a la base de datos de MongoDB
client = MongoClient('localhost', 27017)
db = client.weather_data
weather_collection = db.weather

# Obtener datos de la colección de Weather
weather_data = weather_collection.find()

# Crear listas para almacenar los datos de Weather
cities = []
temperatures = []

# Iterar sobre los datos de Weather y almacenarlos en las listas
for entry in weather_data:
    cities.append(entry['name'])
    temperatures.append(entry['main']['temp'])

# Crear gráfico para los datos de Weather
plt.figure(figsize=(10, 6))
plt.bar(cities, temperatures, color='orange', alpha=0.7)
plt.xlabel('City')
plt.ylabel('Temperature (K)')
plt.title('Temperature by City')
plt.xticks(rotation=0)  # Rotación en 0 grados para etiquetas horizontales
plt.tight_layout()

# Mostrar el gráfico
plt.show()
