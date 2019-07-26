import pytest
from calculator import Calculator

calculator = Calculator()

def test_plus():
    assert calculator.plus(2, 3) == 5
    assert calculator.plus(54, 3) == 57
    assert calculator.plus(22, 3) == 25

def test_minus():
    assert calculator.minus(5, 3) == 2
    assert calculator.minus(5, 1) == 4
    assert calculator.minus(5, 5) == 0

def test_mul():
    assert calculator.mul(5, 4) == 20

def test_divide():
    assert calculator.divide(5, 4) == 1