# Test file for calculator.py

# Imports functions to be tested

from calculator import add, subtract, multiply, divide


class test_calculator:
    def test_add(self):
        assert 4 == add(2, 2)

    def test_subtract(self):
        assert 2 == subtract(4, 2)

    def test_multiply(self):
        assert 100 == multiply(10, 10)

    def test_divide(self):
        assert 5 == divide(25, 5)
