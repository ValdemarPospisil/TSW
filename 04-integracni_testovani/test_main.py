import pytest
from main import main
from services.weather_sevice_stub import WeatherServiceStub
import unittest
from services.weather_service_mock import WeatherServiceMock

def test_main_with_stub(capsys):
    main(use_stub=True)

    captured = capsys.readouterr()
    assert "Teplota v Prague: 20.0°C, Počasí: clear sky" in captured.out

def test_main_with_real_service(capsys):
    main(use_stub=False)

    captured = capsys.readouterr()
    assert "Teplota v Prague:" in captured.out

def test_main_with_mock(capsys):
    main(use_mock=True, api_key="dummy_api_key")

    captured = capsys.readouterr()
    assert "Teplota v Prague:" in captured.out

def test_main_with_mock_no_api_key(capsys):
    main(use_mock=True, api_key=None)
    
    captured = capsys.readouterr()
    assert "Chyba: API klíč není nastaven." in captured.out
