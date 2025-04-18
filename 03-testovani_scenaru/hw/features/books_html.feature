@html
Feature: HTML Testování stránek

  Scenario: Zobrazení titulní stránky
    Given otevřu hlavní stránku
    Then vidím nadpis "Seznam knih"

  Scenario: Zobrazení knihy
    Given otevřu hlavní stránku
    Then vidím knihu "1984" od "George Orwell"

  Scenario: Tlačítko pro přidání knihy
    Given otevřu hlavní stránku
    Then vidím tlačítko s textem "Přidat knihu"
