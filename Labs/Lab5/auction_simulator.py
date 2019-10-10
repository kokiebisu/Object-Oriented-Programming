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
