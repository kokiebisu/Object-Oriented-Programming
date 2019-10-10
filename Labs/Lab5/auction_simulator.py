import random


class Auction:
    """
    Holds the attribute of an Auction object. Sets up the auction for an item with the given
    starting price
    """

    def __init__(self, bidders, item, starting_price):
        """
        :param bidders: a list of participating bidder objects
        :param item: a string representing the name of the item being auctioned
        :param starting_price: an int
        """
        self._bidders = bidders
        self._item = item
        self._starting_price = starting_price

    def start(self):
        print("Starting Auction!!!\n"
              "-------------------\n"
              f"Auctioning {self._item} starting at {self._starting_price}"
              )


class Auctioneer:
    """
    Maintains a list of bidders and notifies when it accepts new bid. Auctioneers
    can accept new bids if it is greater than the highest current bid. When highest
    current bid updates, it will notify all the bidders except for the bidder that
    placed the new bid.
    """

    def __init__(self, highest_current_bid, highest_current_bidder):
        self._highest_current_bid = highest_current_bid
        self._highest_current_bidder = highest_current_bidder
        self._bidders = []

    def register_bidders(self, observer):
        self._bidders.append(observer)

    def __len__(self):
        return len(self._bidders)

    @property
    def highest_current_bid(self):
        return self._highest_current_bid

    @property
    def highest_current_bidder(self):
        return self._highest_current_bidder

    def update_info(self, bid, bidder):
        if self._highest_current_bid != bid:
            self._highest_current_bid = bid
            self._highest_current_bidder = bidder
            self.notify_bidders()

    @property
    def bidders(self):
        return self._bidders

    def notify_bidders(self):
        # notify the observers
        for observer in self._bidders:
            updated_info = observer(self)
            if updated_info != None:
                updated_bidder, updated_bid = updated_info
                print(
                    f"{updated_bidder} bidded ${updated_bid} in response to {self._highest_current_bidder}'s bid of ${self._highest_current_bid}'")
                self.update_info(updated_bid, updated_bidder)
        return [self.highest_current_bidder, self.highest_current_bid]


class Bidder:
    """
    Observer
    callable object -> object that can be called as a function
    Class that holds the attributes of the people who place the bids
    during the auction. Every time the auctioner accepts a bid, all the bidders
    should be notified.
    """

    def __init__(self, name, budget, bid_probability, bid_increase_perc, highest_bid):
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
        self._bid_probability = bid_probability
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = highest_bid

    def __call__(self, auctioneer):
        """
        Allows the bidder to place a new bid with the auctioneer
        :param auctioneer: an auction object
        """
        if self._name != auctioneer.highest_current_bidder:
            if random.random() < self._bid_probability:
                updated_bid = auctioneer._highest_current_bid * self._bid_increase_perc
                if updated_bid < self._budget:
                    self._highest_bid = updated_bid
                    updated_bidder = self._name
                    return [updated_bidder, updated_bid]
            else:
                return None


def main():
    item_name = input("What is the name of the item?\n")
    starting_price = int(input("What is the starting price?\n"))
    auctioneer = Auctioneer(starting_price, "Starting Bid")
    number_of_bidders = int(input("How many bidders are there?\n"))
    for bidder in range(number_of_bidders):
        bidder_name = input("What is the name of the bidder?\n")
        budget = int(input("How much can you spend?\n"))
        bid_probability = random.random()
        bid_increase_percent = random.uniform(1, 2)
        bidder = Bidder(bidder_name, budget, bid_probability,
                        bid_increase_percent, 0)
        auctioneer.register_bidders(bidder)

    auction = Auction(auctioneer.bidders, item_name, starting_price)
    auction.start()
    bidder, bid = auctioneer.notify_bidders()
    if bidder != "Starting Bid":
        print(f"The Winner of the auction is: {bidder} at ${bid}")
    else:
        print(f"Seems like no one was interested with the item_name")

    bidders_result = {
        bidder._name: bidder._highest_bid for bidder in auctioneer._bidders}
    for bidder, bid in bidders_result.items():
        print(f"{bidder}'s highest bid was ${bid}'")


if __name__ == '__main__':
    main()
