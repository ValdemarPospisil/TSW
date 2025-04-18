import pytest
import math

# 2. Test pro hromadné násobení
@pytest.mark.parametrize("numbers, expected", [
    ([2, 3, 4], 24),
    ([1, 1, 1], 1),
    ([5], 5),
])
def test_multiply_many_basic(calc, numbers, expected):
    assert calc.multiply_many(numbers) == expected

# 6. Test záporných čísel
@pytest.mark.parametrize("numbers, expected", [
    ([-1, 2], -2),
    ([-1, -2, -3], -6),
    ([1, -2, -3], 6),
])
def test_multiply_many_negative(calc, numbers, expected):
    assert calc.multiply_many(numbers) == expected

# 8. Test s nekonečnem
@pytest.mark.parametrize("numbers, expected", [
    ([2, math.inf], math.inf),
    ([-2, math.inf], -math.inf),
    ([0, math.inf], math.inf),  # definované chování
])
def test_multiply_many_infinity(calc, numbers, expected):
    assert calc.multiply_many(numbers) == expected

# 10. Vlastní test – test s nulou
@pytest.mark.parametrize("numbers, expected", [
    ([3, 0, 5], 0),
])
def test_multiply_many_with_zero(calc, numbers, expected):
    assert calc.multiply_many(numbers) == expected
