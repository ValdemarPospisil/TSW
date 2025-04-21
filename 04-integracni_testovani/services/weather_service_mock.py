from datetime import datetime


class WeatherServiceMock:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_weather(self, city):
        if not self.api_key:
            return {"error": "API klíč není nastaven."}

        first_letter = city[0].lower()
        if first_letter < "m":
            temperature = 15.0
            description = "sunny"
        else:
            temperature = 10.0
            description = "cloudy"

        current_minute = datetime.now().minute
        temperature += current_minute * 0.1

        return {
            "main": {"temp": temperature, "humidity": 50},
            "weather": [{"description": description}],
        }
