import argparse
import enum


class PokedexMode(enum.Enum):
    """
    Lists the various modes that the Pokedex can run in
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request():
    pass


class Query():
    """
    The query object represents a query to send to retrieve data from the pokedex api.
    The query object comes with certain accompanying configuration options as well
    as a field that holds the result. The attributes are:
        - mode: 'pokemon' or 'ability' or 'move'
        - input: This is the data that needs to be sent as a request.
        - output: This is the method of output that is requested. 
        At this moment the program supports printing to the console
         or writing to another text file.
        - result: Placehodler value to hold the result of the response. This does
        not usually come in with the query.
        - expand: A flag to determine the user wants an expanded version of the details
        - 
    """

    def __init__(self) -> None:
        """
        Initializes Query
        """
        self._mode = None
        self._data = None
        self._input = None
        self._output = None
        self._result = None
        self._expand = None

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return f"Query[ Mode: {self._mode}, Data: {self._data}, Input: {self._input}, Output: {self._output}, Expand: {self._expand}]"


def validate_mode(mode_name: str):
    try:
        if mode_name == "pokemon" or mode_name == "ability" or mode_name == "move":
            return PokedexMode(mode_name)
        else:
            raise Exception
    except Exception as e:
        print("There was an error in validating mode")
        exit()


def convert_to_data(something: str):
    pass


def validate_input_source(input_source: str):
    try:
        if not input_source.endswith('.txt'):
            raise Exception
        # Check is the name/id is valid
        return input_source
    except Exception as e:
        print("The input file extension is invalid")


def validate_output_source(output_source: str):
    try:
        if not output_source.endswith('.txt'):
            raise Exception
        return output_source
    except Exception as e:
        print("The output file extension is invalid")


def accept_args() -> Query:
    """
    Implements the argparse module to accept arguments via the command line.
    This function specifies what these arguments are and parses it into an
    object of type Query. If something goes wrong with provided arguments
    then the function prints an error message and exits the application.
    :return: The object of type Query with all the arguments provided in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", help="The way you want to find your pokemon. It can be either by Pokemon, Ability, Move.")
    parser.add_argument(
        "input", help="As input, the application can take in either a file name (Text file) or a name/id.")
    parser.add_argument(
        "--expanded", help="When this flag is provided, ceratain attributes are expanded. That is the pokedex will do sub-queries to get more information about a partivular attribute. If this flag is not provided, the app will not get the extra information and just print what's provided. ", action='store_true')
    parser.add_argument("--output", default="print",
                        help="The location of output in which the query should be printed to. ")

    try:
        args = parser.parse_args()
        query_ = Query()
        query_._mode = PokedexMode(args.mode)
        query_._input = args.input
        if args.expanded:
            query_._expand = True
        if args.output:
            query_._output = args.output
        return query_
    except Exception as e:
        print(f"Error! Could not read arguments. \n{e}")
        quit()


def main(query_: Query) -> None:
    print(query_)


if __name__ == '__main__':
    query = accept_args()
    main(query)

    # args = parser.parse_args()
    # query_ = Query()
    # query._mode = validate_mode(args.mode)
    # if args.expanded:
    #     self._expand = True
    # something = validate_input_source(args.input)
    # self._data = convert_to_data(something)
    # if args.output:
    #     output = validate_output_source(args.output)
    #     self._output = output
