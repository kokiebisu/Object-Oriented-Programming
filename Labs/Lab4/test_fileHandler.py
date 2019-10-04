from unittest import TestCase
from pathlib import Path
from file_handler import FileHandler, InvalidFileTypeError


class TestFileHandler(TestCase):
    def test_load_not_found_file(self):
        """Tests to see if the file not found error is raised correctly"""
        self.assertRaises(FileNotFoundError,
                          FileHandler.load_data, "../something.json", ".json")

    def test_load_invalid_file_type(self):
        """Tests to see if the invalid file type error is raised correctly"""
        self.assertRaises(InvalidFileTypeError,
                          FileHandler.load_data, '../unittest.xml', '.xml')

    def test_write_lines_with_wrong_data_type(self):
        """Tests to see if the invalid file type error is raised correctly"""
        self.assertRaises(AttributeError,
                          FileHandler.write_lines("../test.txt", []))

    def test_write_lines_correctly(self):
        """Tests to see if the the write lines method works correctly"""
        file_path = "output.txt"
        data = {"Dad": "Father of the children"}
        FileHandler.write_lines(file_path, data)
        self.assertTrue(Path('output.txt').exists())


