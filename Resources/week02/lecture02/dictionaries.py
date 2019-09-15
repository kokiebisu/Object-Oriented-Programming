"""A module depicting some simple dictionary behaviors"""


def main():
    """An example of some dictionary behaviors and looping"""
    my_dictionary = {}
    print(f"Empty Dictionary: {my_dictionary}", end="\n\n")

    my_dictionary = {
        "name": "Luffy",
        "age": 20
    }

    # Adding and accessing elements
    my_dictionary["occupation"] = ["Pirate King", "Professional Eater", "Captain"]
    print(f"Updated dictionary: {my_dictionary}")
    print("Age: {}".format(my_dictionary["age"]), end="\n\n")

    print(f"Keys view: {my_dictionary.keys()}")
    print(f"Values view: {my_dictionary.values()}")
    print(f"Items view: {my_dictionary.items()}", end="\n\n")

    print("Looping over a dictionary")
    for my_key, my_value in my_dictionary.items():
        print(f"Key: {my_key}, Value: {my_value}")


if __name__ == '__main__':
    main()