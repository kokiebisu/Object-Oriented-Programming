""" A simple calculator program that implements a dictionary input map"""


def sum_(a, b):
    """
    Returns the result by summing the two parameters
    :param a: an int or a float
    :param b: an int of a float
    """
    return a + b


def multiply(a, b):
    """
    Returns the result of multiplying the two parameters.
    :param a: an int or a float
    :param b: an int of a float
    """
    return a * b


def divide(a, b):
    """
    Returns the result of dividing the first parameter by the second.
    :param a: an int or a float
    :param b: an int of a float
    """
    return a / b


def subtract(a, b):
    """
    Subtracts the second parameter from the first. Returns the result.
    :param a: an int or a float
    :param b: an int of a float
    """
    return a - b


def main():
    """
    Prints a menu of operations that the user can select from and subsequently
    performs that calculation.
    """
    print("Select from the menu:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    input_map = {
        1: sum_(a, b),
        2: subtract(a, b),
        3: multiply(a, b),
        4: divide(a, b)
    }

    input_map.get(choice, "Invalid input")


if __name__ == "__main__":
    main()

