import argparse


class Pokedex():
    def __init__(self):
        """
        Initializes the Pokedex
        """
        pass

    def __str__(self):
        return "A Pokedex"


class Query():
    """
    The query object represents a query to send to retrieve data from the pokedex api. The query object comes with certain
    accompanying configuration options as well as a field that holds the result. The attributes are:
        - mode: 'pokemon' or 'ability' or 'move'
        - input_file: 
        -

    """


def validate_mode(String: mode_name):
    pass


def validate_input_source(String: input_source):
    pass


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
        "--expanded", help="When this flag is provided, ceratain attributes are expanded. That is the pokedex will do sub-queries to get more information about a partivular attribute. If this flag is not provided, the app will not get the extra information and just print what's provided. ")
    parser.add_argument("--output", default="print",
                        help="The location of output in which the query should be printed to. ")

    try:
        args = parser.parse_args()
        query_ = Query()
        # if (args.mode != "pokemon" and args.mode != "ability" and args.mode != "move"):
        #     raise Exception
        # else:
        #     print(args.mode)
        if validate_mode(args.mode):
            print(args.mode)
        if validate_input_source(args.input):
            print(args.input)
        if args.expanded:
            print(args.expanded)
        if args.output:
            print(args.output)
    except Exception as e:
        print(f"Error! Could not read arguments. \n{e}")
        quit()


if __name__ == '__main__':
    query = accept_args()
