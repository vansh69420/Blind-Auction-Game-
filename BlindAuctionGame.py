from replit import clear


from art import logo
print(logo)
bidding_dictionary = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

            
while not bidding_finished:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid $"))
    bidding_dictionary[name] = bid
    new_bidder = input("If there is anybody wants to bid type 'yes' or if your bid is over then 'no'\n")
    if new_bidder == "no":
        bidding_finished = True
        find_highest_bidder(bidding_dictionary)
    elif new_bidder == "yes":
        clear()
       



        
