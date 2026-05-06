print("Welcome to the Secret Auction Program!")

bids = {}
continue_bidding = "yes"

while continue_bidding == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? AZN "))

    bids[name] = bid

    continue_bidding = input(
        "Are there any other bidders? Type 'yes' or 'no': ").lower()

print("\nAuction results:")

highest_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of {highest_bid} AZN.")