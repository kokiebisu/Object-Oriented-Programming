class Iterable:
    def make_it_iterable(self, object):
        return self.__iter__(object)


iterable = Iterable()
list = ['0', '1', '2', '3']
iterable.make_it_iterable(list)
