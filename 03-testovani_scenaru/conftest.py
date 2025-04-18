import pytest
from calculator import Calculator
from bank import BankAccount

@pytest.fixture
def calc():
    return Calculator()

@pytest.fixture
def account():
    return BankAccount()
