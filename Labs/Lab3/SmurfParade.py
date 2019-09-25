import collections.abc


class SmurfParade:
    def __init__(self, *values):
        self._values = list(values)

    def append(self, name):
        self._values.append(name)

    def __len__(self):
        return len(self._values)

    def __contains__(self, item):
        return item in self._values

    def __getitem__(self, key):
        return self._values[key]

    def __iter__(self):
        return iter(self._values)

    def __str__(self):
        return f"{self._values}"

    # def count(item):
    #     # count the number of items
    #     return

        # def index(item):
        #     # display the index of the given item

        # def __reversed__(self):
        #     # reverse string
        #     return reversed(self)
