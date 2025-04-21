import pytest
from pytest_bdd import scenarios, given, then

scenarios('../features/books_html.feature')


@given('otevřu hlavní stránku')
def open_main_page(browser, base_url):
    browser.visit(base_url)


@then('vidím nadpis "Seznam knih"')
def see_heading(browser):
    assert browser.find_by_tag('h1').first.text == "Seznam knih"


@then('vidím knihu "1984" od "George Orwell"')
def see_book(browser):
    book_divs = browser.find_by_css('.book')
    for book_div in book_divs:
        title = book_div.find_by_tag('h3').first.text
        author_text = book_div.find_by_tag('p').first.text
        if title == "1984" and "George Orwell" in author_text:
            assert True
            return
    assert False, "Kniha '1984' od 'George Orwell' nebyla nalezena"


@then('vidím tlačítko s textem "Přidat knihu"')
def see_add_button(browser):
    assert browser.find_by_id('add-book').first.text == "Přidat knihu"
