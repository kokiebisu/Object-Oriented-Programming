class Dvd:
    def __init__(self, name, release_date, region_code, num_copies):
        self._name = name
        self._release_date = release_date
        self._region_code = region_code
        self._num_copies = num_copies

    def get_name(self):
        return self._name

    def get_release_date(self):
        return self._release_date

    def get_region_code(self):
        return self._region_code

    def get_num_copies(self):
        return self._num_copies

    def set_name(self, name):
        self._name = name

    def set_release_date(self, release_date):
        self._release_date = release_date

    def set_region_code(self, region_code):
        self._region_code = region_code

    def set_num_copies(self, num_copies):
        self._num_copies = num_copies

    name = property(get_name, set_name)
    release_date = property(get_release_date, set_release_date)
    region_code = property(get_region_code, set_region_code)
    num_copies = property(get_num_copies, set_num_copies)

    def __str__(self):
        return f"DVD: {self._name}, Release Date: {self._release_date}, Region Code: {self._region_code}, Number of Copies: {self.num_copies}"
