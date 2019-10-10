""" A module that simulates an auction using Observer patterns"""
import random


class Auction:
    """
    A class that holds the attribute of an Auction object. Sets up the auction for an item with the given
    starting price
    """

    def __init__(self, bidders, item, starting_price):
        """
        Initializes the attributes for an auction instance
        :param bidders: a list of participating bidder objects
        :param item: a string representing the name of the item being auctioned
        :param starting_price: an int
        """
        self._bidders = bidders
        self._item = item
        self._starting_price = starting_price
        self.auctioneer = Auctioneer(starting_price)

    def start(self):
        """
        Starts the auction
        """
        print("Starting Auction!!!\n"
              "-------------------\n"
              f"Auctioning {self._item} starting at ${self._starting_price}"
              )
        self.auctioneer.notify_bidders()


class Auctioneer:
    """
    A class that maintains a list of bidders and notifies when it accepts new bid. Auctioneers
    can accept new bids if it is greater than the highest current bid. When highest
    current bid updates, it will notify all the bidders except for the bidder that
    placed the new bid.
    """

    def __init__(self, value):
        """
        Initializes the attributes for an auctioneer instance
        :param highest_current_bid: a float
        :param highest_current_bidder: a string
        """
        self._highest_current_bid = value
        self._highest_current_bidder = "House start bidder"
        self._bidders = []
        self._result_bidders = {}

    def register_bidders(self, bidder):
        """
        Registers the bidder to be observed
        :param bidder: a bidder object
        """
        self._bidders.append(bidder)

    @property
    def highest_current_bid(self):
        """
        Gets the highest bid being promised
        :return: a float
        """
        return self._highest_current_bid

    @property
    def highest_current_bidder(self):
        """
        Gets the name of the person promising the highest bid
        :return:
        """
        return self._highest_current_bidder

    @highest_current_bidder.setter
    def highest_current_bidder(self, value):
        self._highest_current_bidder = value
        self._highest_current_bid = value._highest_bid
        print("A bid was made!")
        self.notify_bidders()

    @property
    def bidders(self):
        """
        Gets all the bidders participating
        :return: a list
        """
        return self._bidders

    def notify_bidders(self):
        """
        Notifies all the bidders there was an update on the highest bid
        :return: a list
        """
        for bidder in self._bidders:
            bidder(self)


class Bidder:
    """
    A class that holds the attributes of the people who place the bids
    during the auction. Every time the auctioneer accepts a bid, all the bidders
    should be notified.
    """

    def __init__(self, name, budget, bid_increase_perc):
        """
        Initializes the Bidder instance
        :param name: a string
        :param budget: an int
        :param bid_probability: a float
        :param bid_increase_perc: a float
        :param highest_bid: a float
        """
        self._name = name
        self._budget = budget
        self._bid_probability = random.random()
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = 0

    def __call__(self, auctioneer):
        """
        Allows the bidder to place a new bid with the auctioneer
        :param auctioneer: an auction object
        """
        if self != auctioneer.highest_current_bidder:
            if self._budget > auctioneer.highest_current_bid * self._bid_increase_perc:
                if self._bid_probability >= random.random():
                    self._highest_bid = auctioneer.highest_current_bid * \
                        self._bid_increase_perc
                    print(f"{self.name} bidded ${self._highest_bid} in response to "
                          f"{auctioneer.highest_current_bidder} bid of "
                          f"${auctioneer.highest_current_bid}!")

                    auctioneer.highest_current_bidder = self

    @property
    def name(self):
        """
        Gets the name of the bidder
        :return: a string
        """
        return self._name

    @property
    def highest_bid(self):
        """
        Gets the highest bid of that person
        :return: a float
        """
        return self._highest_bid

    def __str__(self):
        return f"{self._name}"


def main():
    """
    Runs the program
    """
    item_name = "vase"
    starting_price = 10
    number_of_bidders = int(input("How many bidders are there?\n"))
    auction = Auction(number_of_bidders, item_name, starting_price)
    for bidder in range(number_of_bidders):
        bidder_name = input("What is the name of the bidder?\n")
        budget = 10000
        bid_increase_percent = 1.6
        auction.auctioneer.register_bidders(
            Bidder(bidder_name, budget, bid_increase_percent, ))
    auction.start()

    results = {
        bidder._name: bidder._highest_bid for bidder in auction.auctioneer.bidders}
    for key, value in results.items():
        print(f"{key}'s highest bid was ${value}")
    print(
        f"The highest bid was {auction.auctioneer.highest_current_bid} by {auction.auctioneer._highest_current_bidder}")


if __name__ == '__main__':
    main()
