# Calculator.py
# Python Application for the myapp project.
# Example Python calculator application

"""
Calculator functions for doing math operations on numbers.
"""


def add(number1, number2):
    """
    Function to add two numbers

    Args:
        number1 (int): First number
        number2 (int): Second number

    Returns:
        int: Sum of number1 + number2

    Raises:
        TypeError: If either number1 or number2 is not an integer
    """
    return number1 + number2


def subtract(number1, number2):
    """
    Function to substract two numbers

    Args:
        number1 (int): First number
        number2 (int): Second number

    Returns:
        int: Substract of number1 - number2

    Raises:
        TypeError: If either number1 or number2 is not an integer
    """
    return number1 - number2


def multiply(number1, number2):
    """
    Function to multiply two numbers

    Args:
        number1 (int): First number
        number2 (int): Second number

    Returns:
        int: Multiply of number1 * number2

    Raises:
        TypeError: If either number1 or number2 is not an integer
    """
    return number1 * number2


def divide(number1, number2):
    """
    Function to divide two numbers

    Args:
        number1 (int): First number
        number2 (int): Second number

    Returns:
        int: Divide of number1 / number2
    Raises:
        TypeError: If either number1 or number2 is not an integer
    """
    return number1 / number2
