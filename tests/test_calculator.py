import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()
    
    def test_add(self, calculator):
        assert calculator.add(3, 5) == 8
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
    
    def test_subtract(self, calculator):
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(1, 1) == 0
        assert calculator.subtract(0, 5) == -5
    
    def test_multiply(self, calculator):
        assert calculator.multiply(3, 5) == 15
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(0, 5) == 0
        print(">> Multiplying ")
        assert calculator.multiply(1,2) == 1
    
    def test_divide(self, calculator):
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(0, 5) == 0
    
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError) as exc_info:
            calculator.divide(1, 0)
        assert str(exc_info.value) == "Cannot divide by zero"
    
    @pytest.mark.parametrize("test_input,expected", [
        ((4, 6), 10),
        ((0, 0), 0),
        ((-1, -1), -2),
    ])
    def test_add_parametrize(self, calculator, test_input, expected):
        assert calculator.add(*test_input) == expected
