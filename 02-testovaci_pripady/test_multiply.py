import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.multiplication
@pytest.mark.simple
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (0, 5, 0),
])
def test_multiply_simple(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.multiplication
@pytest.mark.edge
@pytest.mark.parametrize("a, b, expected", [
    (-2, 3, -6),
    (-3, -3, 9),
    (1e10, 1e-10, 1.0),
    (float('inf'), 1, float('inf')),
])
def test_multiply_edge(calc, a, b, expected):
    assert calc.multiply(a, b) == expected
