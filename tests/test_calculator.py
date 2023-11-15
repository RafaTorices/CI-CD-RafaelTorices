# Test file for calculator.py

"""
File to test the calculator.py file
"""

from calculator import add, subtract, multiply, divide


class TestCalculator:
    """
    Class to test the calculator.py file
    """

    def test_addition(self):
        """
        Function to test the add function
        """
        assert 4 == add(2, 2)

    def test_subtraction(self):
        """
        Function to test the subtract function
        """
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        """
        Function to test the multiply function
        """
        assert 100 == multiply(10, 10)

    def test_division(self):
        """
        Function to test the divide function
        """
        assert 5 == divide(25, 5)