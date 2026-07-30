import calculator
import pytest


def test_add():
    assert calculator.add(2, 3) == 5  # nosec B101


def test_subtract():
    assert calculator.subtract(5, 3) == 2  # nosec B101


def test_multiply():
    assert calculator.multiply(4, 3) == 12  # nosec B101


def test_divide():
    assert calculator.divide(10, 2) == 5  # nosec B101


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

def test_power():
    assert calculator.power(2, 3) == 8  # nosec B101
