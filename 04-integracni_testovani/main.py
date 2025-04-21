from services.weather_service import WeatherService
from services.weather_sevice_stub import WeatherServiceStub
from services.weather_service_mock import WeatherServiceMock
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


def main(use_stub=False, use_mock=False, api_key=None):
    if use_stub:
        service = WeatherServiceStub()
    elif use_mock:
        service = WeatherServiceMock(api_key)
    else:
        service = WeatherService()

    city = "Prague"
    response = service.get_weather(city)

    if "error" in response:
        print(f"Chyba: {response['error']}")
    else:
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        print(f"Teplota v {city}: {temperature}°C, Počasí: {description}")


#   logger = WeatherDataLogger()
#    logger.update_data(city, temperature)
