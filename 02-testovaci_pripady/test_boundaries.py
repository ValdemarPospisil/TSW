import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

# === Hraniční hodnoty pro dělení ===
@pytest.mark.parametrize("a, b, expected", [
    (1, 0, pytest.raises(ValueError)),     # dělení nulou
    (0, 1, 0),                              # 0 děleno nenulovým
    (1e10, 2, 5e9),                         # velké číslo
    (1e-10, 1, 1e-10),                      # velmi malé číslo
])
def test_divide_boundaries(calc, a, b, expected):
    if isinstance(expected, type(pytest.raises(Exception))):
        with expected:
            calc.divide(a, b)
    else:
        result = calc.divide(a, b)
        assert result == expected

# === Hraniční hodnoty pro násobení ===
@pytest.mark.parametrize("a, b, expected", [
    (0, 100, 0),
    (-2**31, 1, -2**31),  # nejmenší int
    (2**31 - 1, 1, 2**31 - 1),  # největší int
    (float("inf"), 1, float("inf")),
    (float("-inf"), 1, float("-inf")),
])
def test_multiply_boundaries(calc, a, b, expected):
    result = calc.multiply(a, b)
    assert result == expected

# === Nečíselné vstupy ===
@pytest.mark.parametrize("a, b", [
    ("a", 1),
    (1, "b"),
    (None, 1),
    ([], {}),
])
def test_add_invalid_types(calc, a, b):
    with pytest.raises(TypeError):
        calc.add(a, b)
