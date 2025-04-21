import requests
import pytest
from pytest_bdd import scenarios, when, then

scenarios("../features/books_api.feature")

# Globální proměnná pro uložení response
response_data = {}


@when('pošlu GET požadavek na "/api/books"')
def get_books(base_url):
    global response_data
    resp = requests.get(f"{base_url}/api/books")
    response_data["response"] = resp
    return resp


@when('pošlu GET požadavek na "/api/books/1"')
def get_book_1(base_url):
    global response_data
    resp = requests.get(f"{base_url}/api/books/1")
    response_data["response"] = resp
    return resp


@when('pošlu GET požadavek na "/api/books/999"')
def get_nonexistent_book(base_url):
    global response_data
    resp = requests.get(f"{base_url}/api/books/999")
    response_data["response"] = resp
    return resp


@then("odpověď obsahuje seznam knih")
def response_contains_books():
    global response_data
    resp = response_data["response"]
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) > 0


@then("odpověď obsahuje knihu s ID 1")
def response_contains_book_1():
    global response_data
    resp = response_data["response"]
    assert resp.status_code == 200
    json_data = resp.json()
    assert isinstance(json_data, dict)
    assert json_data.get("id") == 1


@then("odpověď je 404")
def response_is_404():
    global response_data
    resp = response_data["response"]
    assert resp.status_code == 404
