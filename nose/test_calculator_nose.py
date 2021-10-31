import calculator_nose


def test_add():
    assert calculator_nose.add(1, 9) == 10
    assert calculator_nose.add(4, -9) == -5


def test_subtract():
    assert calculator_nose.subtract(2, 2) == 0
    assert calculator_nose.subtract(10, 0) == 10


def test_multiply():
    assert calculator_nose.multiply(5, 10) != 30
    assert calculator_nose.multiply(5, 10) == 50


def test_division():
    assert calculator_nose.division(3, 3) == 1
    assert calculator_nose.division(15, 5) == 3
