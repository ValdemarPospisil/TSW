import pytest
import os
import time
import signal
import subprocess
from splinter import Browser
import multiprocessing

# Globální proměnná pro uložení procesu Flask aplikace
flask_process = None

def start_flask_app():
    """Spustí Flask aplikaci na pozadí"""
    # Cesta k app.py v nadřazeném adresáři
    app_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")
    # Pokud soubor neexistuje, zkusíme najít ve stejném adresáři
    if not os.path.exists(app_path):
        app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    
    # Spustíme Flask aplikaci
    process = subprocess.Popen(["python", app_path])
    
    # Počkáme, až se aplikace načte
    time.sleep(2)
    return process

@pytest.fixture(scope="session", autouse=True)
def setup_flask():
    """Fixture, která spustí Flask aplikaci před všemi testy a vypne ji po nich"""
    global flask_process
    
    # Spustíme Flask aplikaci
    flask_process = start_flask_app()
    
    yield
    
    # Ukončíme Flask aplikaci
    if flask_process:
        flask_process.terminate()
        flask_process.wait()

@pytest.fixture
def browser():
    """Headless prohlížeč pro testování"""
    # Použijeme Firefox v headless režimu
    options = {"headless": True}
    
    # Vytvoříme instanci prohlížeče - pokud Firefox není dostupný, použijeme Chrome
    try:
        with Browser("firefox", **options) as browser:
            yield browser
    except Exception:
        try:
            with Browser("chrome", **options) as browser:
                yield browser
        except Exception:
            # Pokud ani jeden není dostupný, použijeme bez headless
            with Browser("firefox") as browser:
                yield browser

@pytest.fixture
def base_url():
    """URL adresa, kde běží aplikace"""
    return "http://localhost:5000"
