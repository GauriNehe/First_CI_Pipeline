import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong

def test_armstrong_true():
    assert is_armstrong(153) is True

def test_armstrong_false():
    assert is_armstrong(123) is False

def test_zero_and_single_digit():
    assert is_armstrong(0) is True
    assert is_armstrong(7) is True

def test_negative_returns_false():
    assert is_armstrong(-153) is False

def test_four_digit_armstrong():
    assert is_armstrong(9474) is True