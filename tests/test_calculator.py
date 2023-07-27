import pytest
from src.calculator import Calculator

def test_add():
  calculator = Calculator()
  result = calculator.add(4).result()
  assert result == 4

def test_subtract():
  calculator = Calculator()
  result = calculator.add(4).result()
  assert result == 4

def test_multiply():
  calculator = Calculator()
  result = calculator.multiply(3).result()
  assert result == 0

def test_divide():
  calculator = Calculator()
  result = calculator.add(6).divide(3).result()
  assert result == 2

def test_chained_operations():
  calculator = Calculator()
  result = calculator.add(4).subtract(2).multiply(3).divide(2).result()
  assert result == 3.0

def test_divide_by_zero():
  calculator = Calculator()
  with pytest.raises(ValueError):
      calculator.divide(0)
