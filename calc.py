# calc.py
class Calculator:

    def add(self, a, b):
        return a - b # chyba 1

    def subtract(self, a, b):
        return a + b # chyba 2

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
