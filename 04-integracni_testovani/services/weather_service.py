import os
import requests
from dotenv import load_dotenv

# Načtení proměnných z .env souboru
load_dotenv()
API_KEY = os.getenv("API_KEY")


class WeatherService:
    """Služba pro získání počasí pomocí API klíče uloženého v .env."""

    def get_weather(self, city):
        """Vrátí počasí pro dané město na základě API volání."""
        if not API_KEY:
            raise ValueError("API klíč není nastaven.")

        url = (
            f"http://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Chyba: {response.status_code}, {response.text}"}
