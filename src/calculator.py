# Calculator.py
# Python Application for the myapp project.
# Example Python calculator application

"""
Calculator functions for doing math operations on numbers.
"""


def calculator():
    """
    Function to run the calculator

    Args:
        user_choice (int): User choice

    Returns:
        result (int): Result of the operation

    Raises:
        ValueError: If the user choice is not integer
    """
    while True:
        # Selection of the user
        user_choice = read_user_choice()
        # If not exit, do the operation
        if not is_exit(user_choice):
            # Do the operation
            result = operation(user_choice)
            # Show result in the screen
            print_result(result)
        else:
            # Is exit, so break the loop
            break


def read_user_choice():
    """
    Shows the menu and reads the user choice
    If the user choice is not valid, it will ask again

    Args:
        user_choice (int): User choice

    Returns:
        user_choice (int): User choice

    Raises:
        ValueError: If the user choice is not integer
    """
    # Initialize the user choice as invalid
    user_choice = -1

    # Show the menu until the user choice is valid
    while user_choice == -1:
        print("-------------------")
        print("*** CALCULATOR APP ***")
        print("-------------------")
        print("Select an option:")
        print("-------------------")
        print("1.ADD")
        print("2.SUBTRACT")
        print("3.MULTIPLY")
        print("4.DIVIDE")
        print("-------------------")
        print("0.EXIT")
        print("-------------------")

        # Read the user choice
        try:
            user_choice = int(input("Enter your choice:"))
            # If the user choice is not between 0 and 4 return -1
            if (user_choice < 0) or (user_choice > 4):
                print("Invalid choice. Please try again.")
                user_choice = -1
        except ValueError:  # If the user choice is not valid
            print("Invalid choice. Please try again.")
            user_choice = -1
    # Return the user choice
    return user_choice


def operation(user_choice):
    """
    Function to do the operation selected by the user whith the numbers
    introduced

    Args:
        user_choice (int): User choice
        number1 (int): First number
        number2 (int): Second number

    Returns:
        result (int): Result of the operation

    Raises:
        ValueError: If the user choice is not valid
        TypeError: If either number1 or number2 is not an integer
    """
    # Read the numbers
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))
    # Do the operation selected by the user choice with the numbers introduced
    # If the user choice = 1, do the sum
    if user_choice == 1:
        result = add(number1, number2)
    # If the user choice = 2, do the subtraction
    elif user_choice == 2:
        result = subtract(number1, number2)
    # If the user choice = 3, do the multiplication
    elif user_choice == 3:
        result = multiply(number1, number2)
    # If the user choice = 4, do the division
    elif user_choice == 4:
        result = divide(number1, number2)
    # Return the result
    return result


def is_exit(user_choice):
    """
    Exit the calculator if the user wants to quit

    Args:
        user_choice (int): User choice

    Returns:
        bool: True if the user wants to quit, False otherwise

    Raises:
        ValueError: If the user choice is not valid
    """
    # Return True if the user choice is 0 (EXIT)
    return user_choice == 0


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


def print_result(result):
    """
    Print the result of the operation in the screen

    Args:
        result (int): Result of the operation

    Returns:
        int: Result of the operation

    Raises:
        TypeError: If the result is not an integer
    """
    print("\n\n----------------------")
    print("\n\nRESULT = ")
    print(result)
    print("----------------------\n\n")


def log_error(err):
    """
    Function to log an error

    Args:
        err (Exception): Exception to log

    Returns:
        err (Exception): Exception to log (if the err is an Exception

    Raises:
        Exception: If the err is not an Exception
    """
    print("Unhandled Exception!")
    print(err)


if __name__ == "__main__":
    try:
        calculator()
    except ZeroDivisionError as e:
        log_error(e)
