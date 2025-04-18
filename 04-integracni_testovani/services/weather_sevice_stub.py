class WeatherServiceStub:

    def get_weather(self, city):
        return {
            "main": {
                "temp": 20.0,  
                "humidity": 50  
            },
            "weather": [
                {
                    "description": "clear sky"  
                }
            ]
        }
