import requests
import toml
import os
from dotenv import load_dotenv
from pathlib import Path

# Načtení proměnných z .env souboru
load_dotenv()
API_KEY = os.getenv("API_KEY")


def load_config(file_path=Path(__file__).parent / "config.toml"):
    config = toml.load(file_path)
    return config["locations"]["cities"]


def fetch_weather(city):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    )
    return response.json()


def fetch_all_weather(logger):
    cities = load_config()
    weather_data = []
    for city in cities:
        data = fetch_weather(city)
        logger.log(f"Načteno počasí pro {city}: {data['main']['temp']}°C")
        weather_data.append((city, data))
    return weather_data
