from geopy.geocoders import Nominatim
from fastapi import HTTPException

import logging

# Настройка логгера
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


url = "https://api.open-meteo.com/v1/forecast"

geolocator = Nominatim(user_agent="weather_app_v1.0_by_mefyod", timeout=10)

def looking_for_city(city: str):
    logger.debug(f"Ищем координаты для города: {city}")
    try:
        location = geolocator.geocode(city)
        if location:
            logger.debug(f"Найдены координаты для {city}: latitude={location.latitude}, longitude={location.longitude}")
            return location.latitude, location.longitude
        else:
            logger.error(f"Город {city} не найден сервером Nominatim")
            raise HTTPException(status_code=404, detail=f"Город {city} не найден")
    except Exception as e:
        logger.error(f"Ошибка геокодирования для {city}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ошибка геокодирования для {city}: {str(e)}")
