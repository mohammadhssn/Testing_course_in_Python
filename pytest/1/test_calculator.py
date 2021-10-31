import calculator
import pytest


class TestCalculator:
    def test_add(self):
        assert calculator.add(2, 3) == 5
        assert calculator.add(5, -10) == -5

    def test_subtract(self):
        assert calculator.subtract(10, 3) == 7
        assert calculator.subtract(3, 3) == 0

    def test_multiply(self):
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-3, 3) == -9

    def test_division(self):
        assert calculator.division(4, 4) == 1
        assert calculator.division(10, 5) == 2
        with pytest.raises(ZeroDivisionError):
            calculator.division(99, 0)
