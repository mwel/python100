""" A simple text based representation of a blackjack game"""

############### Blackjack Project #####################

import random
import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


player_count = 0
dealer_count = 0
another_card = True

# deal a set of cards
def deal_player (cards, player_count):
    
        # deal card to player
        card = random.choice(cards)
        print (f"Dealer deals [ {card} ]")
        player_count += card
        print (f"Player count: [ {player_count} ]")
        
        return player_count
    
# deal a card to yourself
def deal_dealer (cards, dealer_count):
    
        card = random.choice(cards)
        dealer_count += card
        print (f"Dealer has dealt to self.")

        return dealer_count


""" GAME FLOW """

# intro
print (logo.logo)

# start game?
start = input (f"Start game? Y/N")
if start != "Y": exit()

# round
while player_count <= 21 and another_card:
    player_count = deal_player(cards, player_count)
    dealer_count = deal_dealer(cards, dealer_count)
    another_card = input("Would you like another card? Y/N")
    if another_card != "Y":
        another_card = False

# Bust?
if player_count > 21:
    print (f"Player count: [ {player_count} ]")
    exit ("BUST! Player is above 21. The house wins.")

# player folds
print(f"Player has decided against more cards. \n Player count is {player_count}. \n Dealer count is {dealer_count}.")
if player_count > dealer_count:
    print (f"Player count: [ {player_count} ]")
    exit("BLACKJACK! Player wins.")
else:
    print (f"Player count: [ {player_count} ]")
    exit("No luck. The house wins.")
