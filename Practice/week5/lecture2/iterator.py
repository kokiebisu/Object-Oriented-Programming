class UpperCaseIterator:
    def __init__(self, string):
        list_of_words = string.split()
        self._words = [word.upper() for word in list_of_words]
        self.index = 0

    def __next__(self):
        """
        Responsible for returning the next element in the container,
        otherwise if its at the end, it raises a StopIterator error.
        :return: word, string
        """
        if self.index == len(self._words):
            raise StopIteration()
        my_word = self._words[self.index]
        self.index += 1
        return my_word

    def __iter__(self):
        return self


class UpperCaseIterable:

    def __init__(self, string):
        self._string = string

    def __iter__(self):
        return UpperCaseIterator(self._string)


def main():
    sentence = UpperCaseIterable("This is a sentence")

    for word in sentence:
        print(word)

    # Wrong Way
    # finished_iteration = False
    # sentence_iterator = iter(sentence)
    # while not finished_iteration:
    #     try:
    #         print(next(sentence_iterator))
    #     except StopIteration:
    #         finished_iteration = True


main()
