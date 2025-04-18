class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self._balance
