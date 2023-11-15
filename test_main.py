# Test file for calculator.py

# Imports functions to be tested

from calculator import add, subtract


class test_calculator:
    def test_add(self):
        assert 4 == add(2, 2)

    def test_subtract(self):
        assert 2 == subtract(4, 2)
