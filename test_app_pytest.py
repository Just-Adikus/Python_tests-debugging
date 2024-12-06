import pytest
from app import factorial, is_prime, gcd

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(1.5)

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(-3) is False

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(-48, 18) == 6
    assert gcd(0, 18) == 18

