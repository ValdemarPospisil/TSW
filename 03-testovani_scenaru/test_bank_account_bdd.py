import pytest
from pytest_bdd import scenarios, given, when, then
from bank import BankAccount

# Načtení scénářů z .feature souboru
scenarios("bank_account.feature")


@pytest.fixture
def account():
    return BankAccount()


# --- GIVEN ---
@given("nový bankovní účet")
def new_account(account):
    return account  # vrací fixture account


@given("bankovní účet se zůstatkem 300 Kč")
def account_with_300(account):
    account.deposit(300)
    return account  # používá stejný objekt account z fixture


# --- WHEN ---
@when("vložím 200 Kč")
def deposit_money(account):
    account.deposit(200)


@when("vyberu 100 Kč")
def withdraw_money(account):
    account.withdraw(100)


@when("vyberu 500 Kč")
def withdraw_too_much(account):
    account.withdraw(500)


# --- THEN ---
@then("zůstatek je 200 Kč")
def check_balance_200(account):
    assert account.get_balance() == 200


@then("zůstatek je 0 Kč")
def check_balance_0(account):
    assert account.get_balance() == 0
