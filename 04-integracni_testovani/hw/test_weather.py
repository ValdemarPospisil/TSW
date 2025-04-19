import weather
from unittest.mock import patch


class SpyLogger:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)


def test_fetch_all_weather_with_spy():
    spy_logger = SpyLogger()
    weather_data = weather.fetch_all_weather(spy_logger)
    assert len(spy_logger.messages) > 0
    assert all("Načteno počasí pro" in msg for msg in spy_logger.messages)


def test_fetch_weather_monkeypatch(monkeypatch):
    def mock_fetch_weather(city):
        return {
            "main": {
                "temp": 20
            }
        }

    monkeypatch.setattr(weather, "fetch_weather", mock_fetch_weather)

    class DummyLogger:
        def __init__(self):
            self.logs = []

        def log(self, msg):
            self.logs.append(msg)

    logger = DummyLogger()
    data = weather.fetch_all_weather(logger)

    assert all(temp[1]["main"]["temp"] == 20 for temp in data)
    assert len(logger.logs) == 3
