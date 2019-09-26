""" This module houses a sequence for smurfs """


class SmurfParade:
    """
    A class that encapsulates a list of smurfs.
    """

    def __init__(self, value):
        """
        Initializes a list of smurfs with smurfs.
        :param values: multiple packed arguments
        """
        self._value = value
        self._next = None

    def append(self, name):
        """
        Adds a smurf to the list.
        :param name: a string
        """
        self._next = name

    def __len__(self):
        """
        Retrieves the number of smurfs in the list
        :return: an int
        """
        count = 0
        flag = True
        while flag == True:
            if self._next:
                count += 1
            else:
                flag = False
        return count

    def __contains__(self, item):
        """
        Checks if a certain item is included in the list
        :param item: a string
        :return: a boolean
        """
        return item in self._smurfs_list

    def __getitem__(self, key):
        """
        Retrieves the element from the list based on the given key
        :param key: an int
        :return: a string
        """
        return self._smurfs_list[key]

    def __iter__(self):
        """
        Creates a iterator that iterates over the SmurfParade class
        :return: an iterable object
        """
        return iter(self._smurfs_list)

    def count(self, item):
        """
        Retrieves the frequency of a certain item
        :param item: a string
        :return: an int
        """
        return self._smurfs_list.count(item)

    def index(self, item):
        """
        Gets the index of an item based on the smurf's name
        :param item: a string
        :return: an int
        """
        return self._smurfs_list.index(item)

    def __reversed__(self):
        """
        Return a list with the position of elements reversed
        :return: a list
        """
        return list(reversed(self._smurfs_list))

    def __str__(self):
        """
        String representation of the created object
        :return: a string
        """
        return f"{self._value}"


def main():
    print('Creating list of Smurfs')
    smurfs = SmurfParade('Bob')
    print(smurfs)

    print("\n")
    print("Append")
    smurfs.append('Ken')
    print(smurfs)

    # print("\n")
    # print("__len__()")
    # print(len(smurfs))

    # print("\n")
    # print("Contains")
    # print('Bob' in smurfs)

    # print("\n")
    # print("__getitem__()")
    # print(smurfs[0])

    # print("\n")
    # print("__iter__()")
    # for i in smurfs:
    #     print(i)

    # print("\n")
    # print("count()")
    # print(smurfs.count('Bob'))

    # print("\n")
    # print("index()")
    # print(smurfs.index('Sam'))

    # print("\n")
    # print("reversed()")
    # print(reversed(smurfs))

    # print(smurfs)


if __name__ == '__main__':
    main()
