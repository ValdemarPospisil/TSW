import pytest
from password_check import is_valid_password

@pytest.mark.parametrize("password, expected", [
    ("StrongPass1", True),           
    ("Short1A", False),              
    ("nouppercase1", False),         
    ("NOLOWERCASE1", False),         
    ("NoNumberHere", False),         
    ("12345678", False),             
])
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected
