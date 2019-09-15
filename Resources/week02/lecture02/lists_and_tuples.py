"""List demo from the lecture"""


def main():
    """
    Some common list and tuple behaviors
    """
    the_dark_side = []
    print(f"Empty list: {the_dark_side}", end="\n\n")

    the_dark_side = ["Darth Vader", "Darth Sidius", "Count Dooku"]
    print("Accessing list elements")
    print(the_dark_side[0])
    print(the_dark_side[-1])
    print(the_dark_side[-2],end="\n\n")

    the_dark_side.append("Kylo Ren")
    the_dark_side.append("Kylo Ren")
    print(f"After Appending: {the_dark_side}")

    popped_string = the_dark_side.pop()
    print(f"Pop: {popped_string}, the_dark_side: {the_dark_side}")

    the_dark_side.sort()
    print(f"Sorted Method: {the_dark_side}")

    the_dark_side.reverse()
    new_list = sorted(the_dark_side)
    print(f"Sorted Function: {new_list}, Original list reversed: {the_dark_side}", end = "\n\n")

    print("Looping over a sequence:")
    for name in the_dark_side:
        print(name)

if __name__ == "__main__":
    main()
