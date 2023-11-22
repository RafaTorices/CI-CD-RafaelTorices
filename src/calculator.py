# Calculator.py
# Example Python calculator application in terminal

"""
Calculator functions for doing math operations on numbers.
"""


def calculator():
    """
    Function to run the calculator

    Args:
        user_choice (int): User choice

    Returns:
        result (int): Int number result of the selected operation
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
        user_choice (int): int number User choice
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
    # If the user choice is valid, return it
    return user_choice


def operation(user_choice):
    """
    Function to do the operation selected by the user whith the numbers
    introduced

    Args:
        user_choice (int): User choice
        number1 (float): First number
        number2 (float): Second number

    Returns:
        result (float): Float number result of the operation
    """
    try:
        # Read the numbers
        number1 = float(input("Enter the first number:"))
        number2 = float(input("Enter the second number:"))
        # Do the operation selected by the user choice with the numbers write
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
    except ValueError:
        return "Invalid number. Please try again."


def is_exit(user_choice):
    """
    Exit the calculator if the user wants to quit

    Args:
        user_choice (int): User choice

    Returns:
        bool: True if the user wants to quit, False otherwise
    """
    # Return True if the user choice is 0 (EXIT)
    return user_choice == 0


def add(number1, number2):
    """
    Function to add two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Sum of number1 + number2
    """
    return number1 + number2


def subtract(number1, number2):
    """
    Function to substract two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Substract of number1 - number2
    """
    return number1 - number2


def multiply(number1, number2):
    """
    Function to multiply two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Multiply of number1 * number2
    """
    return number1 * number2


def divide(number1, number2):
    """
    Function to divide two numbers

    Args:
        number1 (float): First number
        number2 (float): Second number

    Returns:
        float: Divide of number1 / number2
    """
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Division by zero is not allowed !!!!!"


def print_result(result):
    """
    Print the result of the operation in the screen

    Args:
        result (float): Result of the operation

    Returns:
        float: Result of the operation
    """
    print("\n\n----------------------")
    print("\n\nRESULT = ")
    print(result)
    print("----------------------\n\n")


if __name__ == "__main__":
    calculator()
