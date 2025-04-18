import pytest
from pytest_bdd import scenarios, given, then

scenarios('../features/books_html.feature')


@given('otevřu hlavní stránku')
def open_main_page(browser, base_url):
    browser.visit(base_url)


@then('vidím nadpis "Seznam knih"')
def see_heading(browser):
    assert browser.find_by_tag('h1').first.text == "Seznam knih"
