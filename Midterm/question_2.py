""" Module that runs the DeEncryptor Program """
from question_1 import DeEncryptor


def main():
    """ Drives the Program"""
    encrypt = DeEncryptor()
    integer_list = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
    print(encrypt.convert_to_string(integer_list))


if __name__ == '__main__':
    main()