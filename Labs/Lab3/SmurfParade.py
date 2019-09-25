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

    def count(self, item):
        return self._values.count(item)
        # duplicate_count = 0
        # for i in self._values:
        #     if i == item:
        #         duplicate_count += 1
        # return duplicate_count

    def index(self, item):
        return self._values.index(item)

    def __reversed__(self):
        return self._values[::-1]

    def __str__(self):
        return f"{self._values}"
