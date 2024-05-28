import matplotlib.pyplot as plt
from pymongo import MongoClient
import pandas as pd


# Conexión a la base de datos de MongoDB
client = MongoClient('localhost', 27017)
db_weather = client.weather_data
weather_collection = db_weather.weather

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

# Crear la primera figura y el gráfico de barras para temperaturas
plt.figure(figsize=(12, 6))
bars_temp = plt.bar([city + ' Temp' for city in cities], temperatures, color='orange', alpha=0.7, label='Temp')
bars_temp_min = plt.bar([city + ' Min' for city in cities], temp_mins, color='blue', alpha=0.7, label='Min Temp')
bars_temp_max = plt.bar([city + ' Max' for city in cities], temp_maxs, color='green', alpha=0.7, label='Max Temp')

# Añadir etiquetas de temperatura sobre cada barra
for bars in [bars_temp, bars_temp_min, bars_temp_max]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, round(yval, 2), ha='center', va='bottom')

# Configuración del gráfico de temperaturas
plt.xlabel('City and Temperature Type')
plt.ylabel('Temperature (K)')
plt.title('Temperature by City')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Mostrar el gráfico de temperaturas
plt.show(block=False)  # Mostrar sin bloquear la ejecución

# Conexión a la base de datos de MongoDB para estaciones de gasolina
db_gas = client.gasolina_data
gas_station_collection = db_gas.gasolina

# Obtener datos de la colección de estaciones de gasolina (limitar a 10 registros)
gas_station_data = gas_station_collection.find().limit(10)

# Crear listas para almacenar los datos de las estaciones de gasolina
locations = []
regular_prices = []
premium_prices = []
names = []
longitudes = []
latitudes = []

# Iterar sobre los datos de las estaciones de gasolina y almacenarlos en las listas
for entry in gas_station_data:
    locations.append(entry['calle'])
    regular_prices.append(float(entry['regular']) if entry['regular'] else None)
    premium_prices.append(float(entry['premium']) if entry['premium'] else None)
    names.append(entry['razonsocial'])
    longitudes.append(float(entry['longitude']))
    latitudes.append(float(entry['latitude']))

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Location': locations,
    'Regular': regular_prices,
    'Premium': premium_prices,
    'Name': names,
    'Longitude': longitudes,
    'Latitude': latitudes
})

# Crear la segunda figura y el gráfico de precios de combustible regular y premium por ubicación
plt.figure(figsize=(15, 10))
df.plot(kind='bar', x='Location', y=['Regular', 'Premium'], ax=plt.gca(), alpha=0.7)
plt.xlabel('Ubicación')
plt.ylabel('Precio (MXN)')
plt.title('Precios de Combustible Regular y Premium por Ubicación')
plt.xticks(rotation=35,ha='right')
plt.tight_layout()

# Mostrar el gráfico de precios de combustible
plt.show(block=False)  # Mostrar sin bloquear la ejecución

# # Crear un mapa de precios de combustible en diferentes ubicaciones
# map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)

# for i, row in df.iterrows():
#     folium.Marker(
#         location=[row['Latitude'], row['Longitude']],
#         popup=f"{row['Name']}<br>Regular: {row['Regular']}<br>Premium: {row['Premium']}",
#         icon=folium.Icon(color='blue' if row['Regular'] else 'green')
#     ).add_to(map)

# # Guardar el mapa en un archivo HTML
# map.save('map.html')

# Iniciar una sesión interactiva de matplotlib para mantener las ventanas abiertas
plt.show()
