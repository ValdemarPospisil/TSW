@api
Feature: API Testování

  Scenario: Získání všech knih
    When pošlu GET požadavek na "/api/books"
    Then odpověď obsahuje seznam knih

  Scenario: Získání konkrétní knihy
    When pošlu GET požadavek na "/api/books/1"
    Then odpověď obsahuje knihu s ID 1

  Scenario: Neexistující kniha
    When pošlu GET požadavek na "/api/books/999"
    Then odpověď je 404
