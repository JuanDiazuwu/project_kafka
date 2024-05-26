"""
Module to retrieve weather data using OpenWeatherMap API.
"""

import requests
from fastapi import APIRouter

from server.get_coordinates import coordinates
from server.get_api_key import get_api_key
from server.kafka_producer import send_to_kafka

weather = APIRouter()


@weather.get("/weather/{city}")
async def get_weather(city: str):
    """
    Retrieve weather data for a given city.

    Args:
    city (str): The name of the city for which weather data is to be retrieved.

    Returns:
    dict: JSON response containing weather data.
    """
    lat, lon = coordinates(city)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={get_api_key()}"  # pylint: disable=line-too-long
    response = requests.get(url, timeout=10)
    data = response.json()

    send_to_kafka('weathertopic', data)

    return data
