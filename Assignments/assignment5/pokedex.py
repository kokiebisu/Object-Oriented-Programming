import argparse
import enum
import os
import abc
import aiohttp
import asyncio


class PokedexMode(enum.Enum):
    """
    Lists the various modes that the Pokedex can run in
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Query:
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

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input):
        self._input = input

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, output):
        self._output = output

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    @property
    def expand(self):
        return self._expand

    @expand.setter
    def expand(self, expand):
        self._expand = expand

    def accept_args(self):
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
            query_.mode = PokedexMode(args.mode)
            query_.input = args.input
            if args.expanded:
                query_.expand = True
            else:
                query_.expand = False
            if args.output:
                query_._output = args.output
            return query_
        except Exception as e:
            print(f"Error! Could not read arguments. \n{e}")
            quit()

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return f"Query[ Mode: {self._mode}, Data: {self._data}, Input: {self._input}, Output: {self._output}, Expand: {self._expand}]"


class Request():
    """
    Responsible for creating a chain of handlers that will eventually validate
    a query to be sent as a request to retrieve a response from the pokedex api.
    """

    def __init__(self) -> None:
        """
        Sets up the Query and creates a chain of handlers to validate the query.
        """
        self.input_handler = InputHandler()
        self.output_handler = OutputHandler()
        self.request_handler = RequestHandler()
        self.object_handler = ObjectHandler()
        self.print_handler = PrintHandler()

    def execute_query(self, query_: Query) -> bool:
        """
        Responsible for accepting a query and start executing the first handler 
        in the appropriate chain
        :param query_: a Query
        :return: a bool
        """
        result = (None, None)
        # set handlers

        if query_.output == "print":
            self.input_handler.set_handler(self.request_handler)
        else:
            print("entered")
            self.input_handler.set_handler(self.output_handler)
            self.output_handler.set_handler(self.request_handler)
        self.request_handler.set_handler(self.object_handler)
        self.object_handler.set_handler(self.print_handler)
        result = self.input_handler.handle_query(query_)
        if result[1] == False:
            print(result[0])
        else:
            print(result[0])


# def accept_args() -> Query:
#     """
#     Implements the argparse module to accept arguments via the command line.
#     This function specifies what these arguments are and parses it into an
#     object of type Query. If something goes wrong with provided arguments
#     then the function prints an error message and exits the application.
#     :return: The object of type Query with all the arguments provided in it.
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "mode", help="The way you want to find your pokemon. It can be either by Pokemon, Ability, Move.")
#     parser.add_argument(
#         "input", help="As input, the application can take in either a file name (Text file) or a name/id.")
#     parser.add_argument(
#         "--expanded", help="When this flag is provided, ceratain attributes are expanded. That is the pokedex will do sub-queries to get more information about a partivular attribute. If this flag is not provided, the app will not get the extra information and just print what's provided. ", action='store_true')
#     parser.add_argument("--output", default="print",
#                         help="The location of output in which the query should be printed to. ")

#     try:
#         args = parser.parse_args()
#         query_ = Query()
#         query_.mode = PokedexMode(args.mode)
#         query_.input = args.input
#         if args.expanded:
#             query_.expand = True
#         else:
#             query_.expand = False
#         if args.output:
#             query_._output = args.output
#         return query_
#     except Exception as e:
#         print(f"Error! Could not read arguments. \n{e}")
#         quit()


class BaseRequestHandler(abc.ABC):
    """
    Baseclass for all handlers that handler request. This can be
    refactored to work for all request. Each handler can maintain
    a reference to another handler thereby enabling the chain of 
    responsibility pattern.
    """

    def __init__(self, next_handler=None) -> None:
        """
        Initializes the RequestHandler
        :param next_handler: a Handler
        """
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_query(self, query_: Query) -> (str, bool):
        """
        Each handler woudl have a specific implementation of how
        it processes a query.
        :param query_: a Query
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating successful
        handling of the query or not.
        """
        pass

    def set_handler(self, handler) -> None:
        """
        Each handler can invoke another handler at the end of it's
        processing of the rquest. This handler needs to implement the 
        BaseRequestHandler interface.
        :param handler: a BaseRequestHandler
        """
        self.next_handler = handler


class InputHandler(BaseRequestHandler):
    """
    Check if input is valid
    """

    def handle_query(self, query_: Query) -> (str, bool):
        """
        Validates input attribute of query
        :param query_: a Query
        :return: a tuple
        """
        print("Validating Input...")
        if query_.input.lower().endswith('.txt'):
            # Checks if the file exists
            if os.path.exists(query_.input):
                # reads the file and puts into query._data
                if not self.next_handler:
                    return "", True
                return self.next_handler.handle_query(query_)
            else:
                return "File doesn't exist", False
        else:
            query_.data = query_.input
            query_input = None
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_query(query_)


class OutputHandler(BaseRequestHandler):
    """
    Checks if the output file has a valid extension
    :param query_: a Query
    :return: a tuple
    """

    def handle_query(self, query_: Query) -> (str, bool):
        print("Validating Output...")
        if query_.output.lower().endswith('.txt') or query_.output.lower() == "print":
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_query(query_)
        else:
            return "Invalid Output", False


class RequestHandler(BaseRequestHandler):
    """
    Creates the request based on on the given query
    :param query_: a Query
    :precondition: the query must pass all the previous handlers successfully
    :return: a tuple
    """

    def handle_query(self, query_: Query) -> (str, bool):
        print("Creating Request...")
        print(f"Request: {query_}")
        url = f"https://pokeapi.co/api/v2/{query_.mode.value}/{query_.input}"
        query_.data = asyncio.run(self.process_single_request(1, url))
        # print('entered')
        return self.next_handler.handle_query(query_)

    async def process_single_request(self, id_, url: str) -> list:
        """
        """
        async with aiohttp.ClientSession() as session:
            response = await self.get_pokemon_data(id_, url, session)
            return response

    async def get_pokemon_data(self, id_: int, url: str, session: aiohttp.ClientSession) -> dict:
        """
        """
        target_url = url.format(id_)
        response = await session.request(method="GET", url=target_url)
        json_dict = await response.json()
        return json_dict


class ObjectHandler(BaseRequestHandler):
    """
    """

    def handle_query(self, query_: Query) -> (str, bool):
        if query_.mode == PokedexMode.POKEMON:
            pokemon = Pokemon(name=query_.data['name'], id=query_.data['id'], height=query_.data['height'], weight=query_.data['weight'], generation=query_.data['game_indices'],
                              stats=query_.data['stats'][0]['base_stat'], types=query_.data['types'][0]['type']['name'],
                              abilities=query_.data['abilities'], moves=query_.data['moves'][0]['move']['name'])
            query_.data = pokemon
        elif query_.mode == PokedexMode.ABILITY:
            ability = Ability(name=query_.data['name'], id=query_.data['id'], generation=query_.data['generation']['name'], effect=query_.data['effect_entries']
                              [0]['effect'], effect_short=query_.data['effect_entries'][0]['short_effect'], pokemon=query_.data['pokemon'])
            query_.data = ability
        elif query_.mode == PokedexMode.MOVE:
            move = Move(name=query_.data['name'], id=query_.data['id'], generation=query_.data['generation']['name'], accuracy=query_.data['accuracy'], pp=query_.data['pp'],
                        power=query_.data['power'], type_=query_.data['type'], damage_class=query_.data['damage_class']['name'], effect_short=query_.data['effect_entries'][0]['short_effect'])
            query_.data = move
        return self.next_handler.handle_query(query_)


class PrintHandler(BaseRequestHandler):
    """
    """

    def handle_query(self, query_):
        if query_.output.endswith('.txt'):
            with open(f'./{query_.output}', "w") as file:
                file.write(query_.data.__str__())
        else:
            print(query_.data)
        return "", True


class Response():
    def __init__(self, name, id, generation, **kwargs):
        self._name = name
        self._id = id
        self._generation = generation

    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}, Generation: {self._generation}"


class Pokemon(Response):
    def __init__(self, height, weight, stats, types, abilities, moves, **kwargs):
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}, Height: {self._height}, Weight: {self._weight}, Stats: {self._stats}, Types: {self._types}, Abilities: {self._abilities}, Move: {self._moves}"


class Ability(Response):
    def __init__(self, effect, effect_short, pokemon, **kwargs):
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}, Effect: {self._effect}, Effect(Short): {self._effect_short}, Pokemon: {self._pokemon}"


class Move(Response):
    def __init__(self, accuracy, pp, power, type_, damage_class, effect_short, **kwargs):
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type_
        self._damage_class = damage_class
        self._effect_short = effect_short
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()}, Accuracy: {self._accuracy}, PP: {self._pp}, Power: {self._power}, Type: {self._type}, Damage Class: {self._damage_class}, Effect(Short): {self._effect_short}"


def main(query_: Query) -> None:
    """
    Drives the program
    :param query_: a Query
    """
    request = Request()
    request.query_start_handler = InputHandler()
    request.execute_query(query_)


if __name__ == '__main__':
    query = Query()
    query = query.accept_args()
    main(query)
