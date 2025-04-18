import math

class Calculator:
    def multiply_many(self, numbers):
        result = 1
        for num in numbers:
            if math.isinf(num):
                return math.inf if result >= 0 else -math.inf
            result *= num
        return result
