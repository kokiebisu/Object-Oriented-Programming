"""This module deals with decrypting"""


class DeEncryptor:
    """
    This class handles Decrypting inputs being given
    """
    def convert_to_string(self, integer_sequence):
        """
        Converts a sequence of integers into a string based on the ASCII guideline
        :param integer_sequence: a list
        :return: a string
        """
        try:
            if len(integer_sequence) == 0:
                raise
            new_list = [chr(x) for x in integer_sequence]
            some_string = ""
            some_string.
            return ''.join(new_list)
        except TypeError:
            print("There is a non integer element in the sequence!")
        except ValueError:
            print("Must be within range of 0 and 255")
