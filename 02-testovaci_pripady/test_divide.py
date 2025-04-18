import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.division
@pytest.mark.simple
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (0, 3, 0),
])
def test_divide_simple(calc, a, b, expected):
    assert calc.divide(a, b) == expected

@pytest.mark.division
@pytest.mark.edge
@pytest.mark.parametrize("a, b, expected", [
    (-6, 3, -2),
    (5, -2.5, -2.0),
    (1e10, 1e-10, 1e20),
])
def test_divide_edge(calc, a, b, expected):
    assert calc.divide(a, b) == expected

@pytest.mark.division
@pytest.mark.exception
@pytest.mark.parametrize("a, b", [
    (10, 0),
    (1.5, 0.0),
])
def test_divide_by_zero(calc, a, b):
    with pytest.raises(ValueError):
        calc.divide(a, b)
