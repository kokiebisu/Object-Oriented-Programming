"""A module depicting three kinds of string formatting"""


def main():
    """Simple string formatting statements"""
    name = "Goku"
    power = 9000.13956
    age = 20

    print("Hi! My name is {0} and I am {1} years old. My power is {2}".format(name, age, power))
    print(f"Hi! My name is {name} and I am {age} years old. My power is {power}")
    print("Hi! My name is %s and I am %d years old. My power is %.2f (Notice the rounding and float precision)" % (name, age, power))


if __name__ == "__main__":
    main()