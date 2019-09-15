"""Comment module provides an example of a well-commented function."""


def add_ints(a, b):
    """
    Return the sum of the two ints.
    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :return: the sum of the two ints
    """
    return a + b


if __name__ == "__main__":
    print(add_ints(1, 2))
