import pytest
from splinter import Browser


@pytest.fixture
def browser():
    with Browser("firefox") as browser:
        yield browser


@pytest.fixture
def base_url():
    return "http://localhost:5000"
