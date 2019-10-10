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

    def start(self):
        """
        Starts the auction
        """
        print("Starting Auction!!!\n"
              "-------------------\n"
              f"Auctioning {self._item} starting at ${self._starting_price}"
              )


class Auctioneer:
    """
    A class that maintains a list of bidders and notifies when it accepts new bid. Auctioneers
    can accept new bids if it is greater than the highest current bid. When highest
    current bid updates, it will notify all the bidders except for the bidder that
    placed the new bid.
    """

    def __init__(self, highest_current_bid, highest_current_bidder):
        """
        Initializes the attributes for an auctioneer instance
        :param highest_current_bid: a float
        :param highest_current_bidder: a string
        """
        self._highest_current_bid = highest_current_bid
        self._highest_current_bidder = highest_current_bidder
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

    def update_info(self, bid, bidder):
        """
        Updates the highest bid and the highest bidder
        :param bid: a float
        :param bidder: a string
        """
        if self._highest_current_bid != bid:
            self._highest_current_bid = bid
            self._highest_current_bidder = bidder
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
        for bidder in self.bidders:
            bidder(self)


class Bidder:
    """
    A class that holds the attributes of the people who place the bids
    during the auction. Every time the auctioneer accepts a bid, all the bidders
    should be notified.
    """

    def __init__(self, name, budget, bid_increase_perc, highest_bid):
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
        self._highest_bid = highest_bid

    def __call__(self, auctioneer):
        """
        Allows the bidder to place a new bid with the auctioneer
        :param auctioneer: an auction object
        """
        if self == auctioneer.highest_current_bidder:
            pass
        elif self._budget < auctioneer.highest_current_bid * self._bid_increase_perc:
            auctioneer._highest_current_bid = self.highest_bid
            auctioneer.bidders.remove(self)
        else:
            if self._bid_probability < random.random():
                bid_amount = auctioneer.highest_current_bid * self._bid_increase_perc
                print(f"{self.name} has bidded ${bid_amount} in response"
                      f" to {auctioneer.highest_current_bidder} bid of {auctioneer.highest_current_bid}"
                      )
                auctioneer._highest_current_bidder = self._name
                auctioneer._highest_current_bid = bid_amount
                if bid_amount > self._highest_bid:
                    self._highest_bid = bid_amount
        auctioneer._result_bidders[self._name] = auctioneer._highest_current_bid

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


def main():
    """
    Runs the program
    """
    item_name = input("What is the name of the item?\n")
    starting_price = int(input("What is the starting price?\n"))
    auctioneer = Auctioneer(starting_price, "Starting Bid")
    number_of_bidders = int(input("How many bidders are there?\n"))
    for bidder in range(number_of_bidders):
        bidder_name = input("What is the name of the bidder?\n")
        budget = int(input("How much can you spend?\n"))
        bid_increase_percent = float(input("What is the increase percentage?"))
        bidder = Bidder(bidder_name, budget, bid_increase_percent, 0)
        auctioneer.register_bidders(bidder)
    auction = Auction(auctioneer.bidders, item_name, starting_price)
    auction.start()
    while len(auctioneer.bidders) > 1:
        auctioneer.notify_bidders()
    for bidder, bid in auctioneer._result_bidders.items():
        print(f"{bidder}'s highest bid was ${bid}")


if __name__ == '__main__':
    main()
