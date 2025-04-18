import requests
import pytest
from pytest_bdd import scenarios, when, then

scenarios('../features/books_api.feature')


@when('pošlu GET požadavek na "/api/books"')
def get_books(base_url):
    return requests.get(f'{base_url}/api/books')


@then('odpověď obsahuje seznam knih')
def response_contains_books(get_books):
    response = get_books
    assert response.status_code == 200
    assert isinstance(response.json(), list)
