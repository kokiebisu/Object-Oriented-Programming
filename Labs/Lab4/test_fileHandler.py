from unittest import TestCase
from file_handler import FileHandler
from file_handler import InvalidFileTypeError
from pathlib import Path


class TestFileHandler(TestCase):
    def test_load_not_found_file(self):
        """Test if file not found error is handled properly."""
        self.assertRaises(FileNotFoundError,
                          FileHandler.load_data("../something.json", "json"))

    def test_load_invalid_file_type(self):
        """Test if invalid file type error is handled properly."""
        print(FileHandler.load_data("../unittest.xml", ".xml"))
        self.assertRaises(InvalidFileTypeError,
                          FileHandler.load_data("../unittest.xml", ".xml"))

    def test_write_lines_with_wrong_data_type(self):
        """Test if attribute error is handled properly."""
        self.assertRaises(AttributeError,
                          FileHandler.write_lines("../test.txt", []))

    def test_write_lines_correctly(self):
        """Test if the program creates a new text file as an output."""
        file_path = "output.txt"
        data = {"Dad": "Father of the children"}
        FileHandler.write_lines(file_path, data)
        self.assertTrue(Path('output.txt').exists())


