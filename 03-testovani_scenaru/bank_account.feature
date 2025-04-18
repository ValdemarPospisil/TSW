Feature: Bank Account

  Scenario: Vklad peněz na účet
    Given nový bankovní účet
    When vložím 200 Kč
    Then zůstatek je 200 Kč

  Scenario: Úspěšný výběr peněz
    Given bankovní účet se zůstatkem 300 Kč
    When vyberu 100 Kč
    Then zůstatek je 200 Kč

  Scenario: Neúspěšný výběr peněz
    Given nový bankovní účet
    When vyberu 500 Kč
    Then zůstatek je 0 Kč
