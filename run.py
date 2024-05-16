# import random for shuffling the cards
import random 

# Using balsamiq I have created a function flow for the game 
# functions follow the logic of each stage of the game 
# I have added the function layout below
# I have added docstrings above each function for description

"""
- Display's the rules of the game to the user.
- The function uses primarily print statements.
- A call to the next function. 
"""

def display_rules():
    print("WELCOME TO BLACK JACK!\n") 
    print("RULES: ")
    print("To win and beat the dealer you need to get to 21 without going over.")
    print("Card values of King, Queen, and Jack are worth 10. Ace can be worth either 1 or 11 and the other cards are worth their presented number.")
    print("Hit will grant you another card. Stand will keep your current hand.")
    print("The dealer will hit until they reach 17 or higher.")
    print("If you and the dealer tie, this is called a push and no one wins.\n")
    create_deck()
    

"""
- A card game needs a deck so this creates the game deck
- The function uses lists and applies the random module for shuffling
"""
def create_deck():
    values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [value + 'of' + suit for values in values for suits in suits]
    random.shuffle(deck)
    return deck

# def deal_cards():

# def players_turn():

# def dealers_turn():

# def calculate_hand()

# def calculate_winner():

# def show_winner():

# def play_again():

# Calling first function to start game
display_rules()