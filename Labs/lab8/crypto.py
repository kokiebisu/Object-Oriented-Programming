from des import DesKey
import argparse
import abc
import enum
import os.path
import ast


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self) -> None:
        """
        Initializes Request
        """
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        print(args)
        request_ = Request()
        request_.encryption_state = CryptoMode(args.mode)
        request_.data_input = args.string
        request_.input_file = args.file
        request_.output = args.output
        request_.key = args.key
        print(request_)
        return request_
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class BaseRequestHandler(abc.ABC):
    """
    Baseclass for all handlers that handle request. This can be
    refactored to work for all requests. Each handler can maintain a
    reference to another handler thereby enabling the chain of
    responsibility pattern.
    """

    def __init__(self, next_handler=None) -> None:
        """
        Initalizes the RequestHandler
        :param next_handler: a Handler
        """
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request_: Request) -> (str, bool):
        """
        Each handler would have a specific implementation of how it
        processes a request.
        :param request_: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the request or not.
        """
        pass

    def set_handler(self, handler) -> None:
        """
        Each handler can invoke another handler at the end of it's
        processing of the request. This handler needs to implement the
        BaseRequestHandler interface.
        :param handler: a BaseRequestHandler
        """
        self.next_handler = handler


class KeyHandler(BaseRequestHandler):
    """
    Checks if the key attribute of the request has the length of either 8, 16 or 24
    """

    def handle_request(self, request_: Request) -> (str, bool):
        """
        Validates key attribute of request
        :param request_: a Request
        :return: a tuple
        """
        print("Validating Key...")
        if len(request_.key) == 8 or len(request_.key) == 16 or len(request_.key) == 24:
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_request(request_)
        else:
            return "Key must be a length of either 8, 16, 24", False


class FileHandler(BaseRequestHandler):
    """
    Checks if the filename has an extension of .txt
    """

    def handle_request(self, request_: Request) -> (str, bool):
        """
        Validates input_file attribute of request
        :param request_: a Request
        :return: a tuple
        """
        print("Validating File...")
        if request_.input_file:
            if os.path.exists(request_.input_file):
                if request_.input_file.lower().endswith('.txt'):
                    if not self.next_handler:
                        return "", True
                    else:
                        return self.next_handler.handle_request(request_)
                else:
                    return "Wrong extension", False
            else:
                return "File doesn't exist", False
        else:
            return self.next_handler.handle_request(request_)


class OutputFileHandler(BaseRequestHandler):
    """
    Checks if the output filename is valid
    """

    def handle_request(self, request_: Request) -> (str, bool):
        """
        Validates output attribute of request
        :param request_: a Request
        :return: a tuple
        """
        print("Validating Output...")
        if request_.output == 'print' or request_.output.lower().endswith('.txt'):
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request_)
        else:
            return "Invalid Output", False


class ModeHandler(BaseRequestHandler):
    """
    Checks if the mode is valid
    """

    def handle_request(self, request_: Request) -> (str, bool):
        """
        Validates encryption state attribute of request
        :param request_: a Request
        :return: a tuple
        """
        print("Validating Mode...")
        if request_.encryption_state == CryptoMode.EN or request_.encryption_state == CryptoMode.DE:
            if not self.next_handler:
                return "", True
            else:
                return self.next_handler.handle_request(request_)
        else:
            return "Invalid Mode", False


class EncryptHandler(BaseRequestHandler):
    """
    Responsible for encrypting the request
    """

    def handle_request(self, request_: Request):
        """
        Encrypts either the given string or file
        :param request_: a Request
        :return: a tuple
        """
        print("Encrypting...")
        key = DesKey(request_.key.encode('utf-8'))
        if request_.data_input and request_.input_file:
            return "Choose either a text file or a string to encrypt!!", False
        elif request_.data_input:
            request_.result = key.encrypt(request_.data_input.encode('utf-8'), padding=True)
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_request(request_)
        elif request_.input_file:
            with open(request_.input_file, 'r') as file:
                data = file.read()
                request_.result = key.encrypt(
                    data.encode('utf-8'), padding=True)
                if not self.next_handler:
                    return "", True
                return self.next_handler.handle_request(request_)
        else:
            return self.next_handler.handle_request(request_)


class DecryptHandler(BaseRequestHandler):
    """
    Responsible for decrypting the request
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Decrypts either the given string or file
        :param request: a Request
        :return: a tuple
        """
        print("Decrypt Reading")
        key = DesKey(request.key.encode('utf-8'))
        if request.data_input:
            data = r"{0}".format(request.data_input)
            data = ast.literal_eval(data)
            request.result = key.decrypt(data, padding=True).decode('utf-8')
        else:
            with open(request.input_file, "r") as file:
                data = file.read()
                data = ast.literal_eval(data)
                request.result = key.decrypt(data, padding=True).decode('utf-8')
        if not self.next_handler:
            return "", True
        return self.next_handler.handle_request(request)


class OutputtingHandler(BaseRequestHandler):
    """
    Responsible for outputting the encrypted/decrypted content to the given location
    """
    def handle_request(self, request_: Request) -> (str, bool):
        """
        Validates in what way user wants to output the processed data and implements it
        :param request_: a Request
        :return: a tuple
        """
        print("Checking Output...")
        if request.output != 'print':
            with open(request.output, "w") as text_file:
                text_file.write(request.result)
            return "Successfully processed to file", True
        else:
            return f"Successfully processed: {request.result}", True


class Crypto:
    """
    Responsible for creating a chain of handlers that will
    eventually validate a given Request and handler it one by one. 
    """
    def __init__(self) -> None:
        """
        Sets up the enrolment system and creates a chain of handlers.
        """
        self.encryption_start_handler = None
        self.decryption_start_handler = None

        self.key_handler = KeyHandler()
        self.file_handler = FileHandler()
        self.mode_handler = ModeHandler()
        self.output_handler = OutputFileHandler()
        self.encrypt_handler = EncryptHandler()
        self.decrypt_handler = DecryptHandler()
        self.outputting_handler = OutputtingHandler()

    def execute_request(self, request_: Request) -> bool:
        """
        Responsible for accepting a request and start executing the first handler
        in the appropriate chain
        :param request_: a Request
        :return: a bool
        """
        result = (None, None)

        if self.encryption_start_handler:
            self.encryption_start_handler.set_handler(self.file_handler)
            self.file_handler.set_handler(self.mode_handler)
            self.mode_handler.set_handler(self.output_handler)
            self.output_handler.set_handler(self.encrypt_handler)
            self.encrypt_handler.set_handler(self.outputting_handler)
            result = self.encryption_start_handler.handle_request(request_)
        elif self.decryption_start_handler:
            self.decryption_start_handler.set_handler(self.file_handler)
            self.file_handler.set_handler(self.mode_handler)
            self.mode_handler.set_handler(self.output_handler)
            self.output_handler.set_handler(self.decrypt_handler)
            self.decrypt_handler.set_handler(self.outputting_handler)
            result = self.decryption_start_handler.handle_request(request_)

        if result[1]:
            print(result[0])
            return True
        else:
            print(result[0])
            return False


def main(request_: Request) -> None:
    """
    Drive the program
    :param request_: a Request
    """
    print(request_.encryption_state)
    if request_.encryption_state == CryptoMode.EN:
        crypto = Crypto()
        crypto.encryption_start_handler = KeyHandler()
        crypto.execute_request(request_)
    elif request_.encryption_state == CryptoMode.DE:
        crypto = Crypto()
        crypto.decryption_start_handler = KeyHandler()
        crypto.execute_request(request_)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
