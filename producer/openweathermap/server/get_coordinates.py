"""
Module to retrieve coordinates for a given city.
"""

from geopy.geocoders import Nominatim


def coordinates(city_name: str) -> tuple[str, str]:
    """
    Retrieve the coordinates (latitude and longitude) for a given city name.

    Args:
    city_name (str): The name of the city for which coordinates are to be retrieved.

    Returns:
    tuple[str, str]: A tuple containing latitude and longitude as strings.
    """
    geolocator = Nominatim(user_agent="uwu")
    location = geolocator.geocode(city_name)

    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude
