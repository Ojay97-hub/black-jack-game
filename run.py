# import random for shuffling of cards
import random

# Using balsamiq I have created a function flow for the game
# functions follow the logic of each stage of the game
# I have added the function layout below
# I have added docstrings above each function for description

"""
- Display's the rules of the game to the user.
- The function uses primarily print statements.

"""


def display_rules():
    # aware of the amount of prints - was to try and fix the long line issue
    print("WELCOME TO BLACK JACK!\n")
    print("RULES: ")
    print("To win and beat the dealer you need")
    print("to get to 21 without going over.")
    print("Card values of King, Queen, and Jack are worth 10.")
    print("Ace can be worth")
    print("either 1 or 11 and the other cards")
    print("are worth their presented number.")
    print("Hit will grant you another card.")
    print("Stand will keep your current hand.")
    print("The dealer will hit until they reach 17 or higher.")
    print("If you and the dealer tie,")
    print("this is called a push and no one wins.\n")
    create_deck()


"""
- A card game needs a deck so this creates the game deck.
- The function uses lists and applies the random module for shuffling.

"""


def create_deck():
    values = ['ace', 'king', 'queen', 'jack', '10', '9',
              '8', '7', '6', '5', '4', '3', '2']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [value + ' of ' + suit for value in values for suit in suits]
    random.shuffle(deck)
    deal_cards(deck)
    return deck


"""
- Calculate hand function is to assess the value of the hands dealt.
- Contains a while loop.
- Contains list iteration with for loop.
- Conditional statements for the ace calculations.

"""


def calculate_hand(hand):
    total = 0
    num_aces = 0
    for card in hand:
        if card['value'] in ['King', 'Queen', 'Jack']:
            total += 10
        elif card['value'] == 'Ace':
            num_aces += 1
            total += 11
        else:
            total += int(card['value'])
        while total > 21 and num_aces:
            total -= 10
            num_aces -= 1
        return total


"""
- This deal_cards function is to deal cards to player and dealer
- List manipulation is applied

"""


def deal_cards(deck, nums_cards=2):
    # empty lists as hands
    player_hand = []
    dealer_hand = []
    for _ in range(nums_cards):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


# def players_turn():

# def dealers_turn():

# def calculate_winner():

# def show_winner():

# def play_again():


# main function to start game
def main():
    display_rules()
    create_deck()
    calculate_hand()
    deal_cards()


main()
