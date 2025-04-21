import pytest
import json
from bs4 import BeautifulSoup
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_rescode(client):
    expected = 200
    outcome = client.get("/home").status_code
    assert outcome == expected


def test_home_content(client):
    response = client.get("/home")
    soup = BeautifulSoup(response.data, "html.parser")
    header = soup.find("h1").text
    paragraph = soup.find("p").text

    assert header == "Best Website"
    assert paragraph == "This is the best website ever!"


def test_api_author(client):
    expected = {"author": "John Doe"}
    response = client.get("/api/author")
    outcome = json.loads(response.data)
    assert outcome == expected
