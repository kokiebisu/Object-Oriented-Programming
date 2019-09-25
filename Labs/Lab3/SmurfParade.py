class SmurfParade:
    """
    A class that encapsulates a list of smurfs.
    """
    def __init__(self, *values):
        """
        Initializes a list of smurfs with smurfs.
        :param values: multiple packed arguments
        """
        self._values = list(values)

    def append(self, name):
        """
        Adds a smurf to the list.
        :param name: a string
        """
        self._values.append(name)

    def __len__(self):
        """
        Retrieves the number of smurfs in the list
        :return: an int
        """
        return len(self._values)

    def __contains__(self, item):
        """
        Checks if a certain item is included in the list
        :param item: a string
        :return: a boolean
        """
        return item in self._values

    # Not sure about this, is key the index?

    # def __getitem__(self, key):
    #     """
    #     Retrieves the element from the list based on the given key
    #     :param key: an int
    #     :return: a string
    #     """
    #     return self._values[key]

    def __iter__(self):
        """
        Creates a iterator that iterates over the SmurfParade class
        :return: an iterable object
        """
        return iter(self._values)

    def count(self, item):
        """
        Retrieves the frequency of a certain item
        :param item: a string
        :return: an int
        """
        return self._values.count(item)
        # duplicate_count = 0
        # for i in self._values:
        #     if i == item:
        #         duplicate_count += 1
        # return duplicate_count

    def index(self, item):
        """
        Gets the index of an item based on the smurf's name
        :param item: a string
        :return: an int
        """
        return self._values.index(item)

    def __reversed__(self):
        """
        Return a list with the position of elements reversed
        :return: a list
        """
        return self._values[::-1]

    def __str__(self):
        """
        String representation of the created object
        :return:
        """
        return f"{self._values}"


def main():
    smurfs = SmurfParade('Bob', 'Sam', 'Ken')

    smurfs.append('Ken')

    print(smurfs)

    print(smurfs.__len__())

    print(smurfs.__contains__('Bob'))

    print(smurfs.__getitem__(0))

    smurfs_iterator = smurfs.__iter__()
    for i in smurfs_iterator:
        print(i)

    print(smurfs.count('Bob'))

    print(smurfs.index('Sam'))

    print(smurfs.__reversed__())


if __name__ == '__main__':
    main()
