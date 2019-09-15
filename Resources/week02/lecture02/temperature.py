"""A module that depicts class properties in action"""


class Temperature:
    """A simple temperature class to depict how properties work"""

    def __init__(self, fahrenheit):
        """
        Initializes the temperature in fahrenheit
        :param fahrenheit: an int or float
        """
        self._temp = fahrenheit

    def get_temp(self):
        """
        Returns the temperature as a formatted string
        :return: a string
        """
        return f"{str(self._temp)} F"

    def set_temp(self, fahrenheit):
        """
        Sets the temperature if its a positive integer or float
        :param fahrenheit: an int or a float
        """
        if fahrenheit > 0:
            self._temp = fahrenheit

    temp = property(get_temp, set_temp)


def main():
    classroom_temp = Temperature(60)
    print(f"The temperature in the classroom is {classroom_temp.temp}")
    classroom_temp.temp = -10
    print(f"The new temperature in the classroom is {classroom_temp.temp}")


if __name__ == "__main__":
    main()
