import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1, 2, 3, id="positive"),
        pytest.param(-1, -1, -2, id="negative"),
        pytest.param(0, 0, 0, id="zeros"),
        pytest.param(1e10, 1e10, 2e10, id="large_floats"),
    ],
)
def test_add_param(calc, a, b, expected):
    result = calc.add(a, b)
    assert result == expected


def test_add_positive_numbers(calc):
    # Arrange
    a, b = 2, 3

    # Act
    result = calc.add(a, b)

    # Assert
    assert result == 5


def test_add_negative_numbers(calc):
    # Arrange
    a, b = -1, -4

    # Act
    result = calc.add(a, b)

    # Assert
    assert result == -5
