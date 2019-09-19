class Journal:
    def __init__(self, name, issue_number, publisher, num_copies):
        self._name = name
        self._issue_number = issue_number
        self._publisher = publisher
        self._num_copies = num_copies

    def get_name(self):
        return self._name

    def get_issue_number(self):
        return self._issue_number

    def get_publisher(self):
        return self._publisher

    def get_num_copies(self):
        return self._num_copies

    def set_name(self, name):
        self._name = name

    def set_issue_number(self, issue_number):
        self._issue_number = issue_number

    def set_publisher(self, publisher):
        self._publisher = publisher

    def set_num_copies(self, num_copies):
        self._num_copies = num_copies

    name = property(get_name, set_name)
    issue_number = property(get_issue_number, set_issue_number)
    publisher = property(get_publisher, set_publisher)
    num_copies = property(get_num_copies, set_num_copies)

    def __str__(self):
        return f"Journal: {self.name}, Issue Number: {self.issue_number}, Publisher: {self.publisher}, Number of Copies: {self.num_copies}"
