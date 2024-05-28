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
temp_mins = []
temp_maxs = []

# Iterar sobre los datos de Weather y almacenarlos en las listas
for entry in weather_data:
    cities.append(entry['name'])
    temperatures.append(entry['main']['temp'])
    temp_mins.append(entry['main']['temp_min'])
    temp_maxs.append(entry['main']['temp_max'])

# Crear gráfico de barras
plt.figure(figsize=(12, 6))

# Crear barras para cada tipo de temperatura
bars_temp = plt.bar([city + ' Temp' for city in cities], temperatures, color='orange', alpha=0.7, label='Temp')
bars_temp_min = plt.bar([city + ' Min' for city in cities], temp_mins, color='blue', alpha=0.7, label='Min Temp')
bars_temp_max = plt.bar([city + ' Max' for city in cities], temp_maxs, color='green', alpha=0.7, label='Max Temp')

# Añadir etiquetas de temperatura sobre cada barra
for bars in [bars_temp, bars_temp_min, bars_temp_max]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, round(yval, 2), ha='center', va='bottom')

# Configuración del gráfico
plt.xlabel('City and Temperature Type')
plt.ylabel('Temperature (K)')
plt.title('Temperature by City')
plt.xticks(rotation=45, ha='right')
plt.legend()

# Ajustar espaciado
plt.tight_layout()

# Mostrar el gráfico
plt.show()
