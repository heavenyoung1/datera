from fastapi import APIRouter, HTTPException
from define_city import looking_for_city
import openmeteo_requests
from retry_requests import retry
import requests_cache
import logging

# Настройка логгера
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Настройка клиента Open-Meteo API с кэшем и повторной попыткой при ошибке
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

router = APIRouter(tags=["weather"])

@router.get("/getWeather/{city}")
def get_weather(city: str):
    logger.debug(f"Получаем координаты для города: {city}")
    # Получаем координаты города
    try:
        latitude, longitude = looking_for_city(city)
        logger.debug(f"Координаты для {city}: latitude={latitude}, longitude={longitude}")
    except Exception as e:
        logger.error(f"Ошибка получения координат для {city}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Ошибка получения координат для {city}: {str(e)}")

    # Параметры для Open-Meteo API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True  # Запрашиваем текущую погоду
    }
    logger.debug(f"Параметры запроса: {params}")

    try:
        # Выполняем запрос к Open-Meteo API
        responses = openmeteo.weather_api(url="https://api.open-meteo.com/v1/forecast", params=params)
        response = responses[0]

        # Извлекаем данные о текущей погоде
        current_weather = response.Current()
        weather_data = {
            "temperature": f"{current_weather.Variables(0).Value()}°C",
            "windspeed": f"{current_weather.Variables(1).Value()} км/ч",
            "winddirection": f"{current_weather.Variables(2).Value()}°"
        }
        return {
            "city": city,
            "coordinates": {"latitude": latitude, "longitude": longitude},
            "weather": weather_data
        }
    except Exception as e:
        logger.error(f"Ошибка получения погоды для {city}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения погоды для {city}: {str(e)}")