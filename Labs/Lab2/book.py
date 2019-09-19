class Book:
    def __init__(self, title, call_number, author, num_copies):
        self._title = title
        self._call_number = call_number
        self._author = author
        self._num_copies = num_copies

    def get_title(self):
        return self._title

    def get_call_number(self):
        return self._call_number

    def get_author(self):
        return self._author

    def get_num_copies(self):
        return self._num_copies

    def set_title(self):
        return self._title

    def set_call_number(self):
        return self._call_number

    def set_author(self):
        return self._author

    def set_num_copies(self):
        return self._num_copies

    title = property(get_title, set_title)
    call_number = property(get_call_number, set_call_number)
    author = property(get_author, set_author)
    num_copies = property(get_num_copies, set_num_copies)

    def __str__(self):
        return f"Book: {self._title}, Call Number: {self._call_number}, Author: {self._author}, Number of Copies: {self._num_copies}"

    def check_availability(self):
        return self.num_copies > 0
