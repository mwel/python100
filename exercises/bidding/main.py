from bidding import art

print(art)

items_for_sale = [
    {'Vase': 5000},
    {'Painting': 10000},
    {'Sword': 2000}
]


def bid():
    # Print list of items for sale
    print(f"Items for sale: {items_for_sale}")
    # Ask what bidder wants to bid for
    item = input("What item would you like to bid for?")
    # Initialize a dictionary to store bids
    bids = {}
    
    # Loop over the list of items for sale
    for item_dict in items_for_sale:
        # Check if the item is for sale
        if item in item_dict:
            # Fetch minimum bid from the respective dictionary
            minimum_bid = item_dict[item]
            print(f"The item for sale is {item} at a minimum bid of {minimum_bid}.")
            start = input("Would you like to bid? Y/N ")
            
            # If the bidder wants to bid, start the bidding process
            if start == "Y":
                # Ask for bidder's name
                name = input("What is your name?")
                last_bid = minimum_bid
                new_bid = 0
                
                # Display the current bid (last_bid) and get the new bid from the bidder
                print(f"Bid for {item} is currently at {last_bid}.")
                while new_bid <= last_bid:
                    new_bid = int(input("Place your bid in USD."))
                    if new_bid <= last_bid:
                        exit_choice = input("Bid too low. Bid again or enter 'Q' to quit.")
                        if exit_choice == 'Q':
                            print("Thanks for bidding. You have not placed a valid bid.")
                            break
                    else:
                        last_bid = new_bid
                        # Store the bidder's name and bid in the 'bids' dictionary
                        bids[name] = new_bid  
                
                print(f"All Bids: {bids}")
                
                # Find the highest bid and bidder
                highest_bid = max(bids.values())
                highest_bidder = [name for name, bid in bids.items() if bid == highest_bid]
                print(f"Highest bid for {item} is {highest_bid} by {', '.join(highest_bidder)}")
            
            else:
                print("No bids were placed for this item.")
        else:
            print("Item not for sale. Please choose another.")

# CALL
bid()
