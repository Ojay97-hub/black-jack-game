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
    print("WELCOME TO BLACK JACK!\n")
    print("RULES: ")
    print("- To win and beat the dealer you need to get to 21 without going over.")
    print("- Card values of King, Queen, and Jack are worth 10.")
    print("- Ace can be worth either 1 or 11.")
    print("- Other cards are worth their presented number.")
    print("- Hit will grant you another card.")
    print("- Stand will keep your current hand.")
    print("- The dealer will hit until they reach 17 or higher.")
    print("- If you and the dealer tie, this is called a push and no one wins.\n")
    create_deck()


"""
- A card game needs a deck so this creates the game deck.
- The function uses lists and applies the random module for shuffling.

"""


def create_deck():
    values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # making the 52 cards
    deck = [{'value': value, 'suit': suit} for value in values for suit in suits]
    # shuffles the deck
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
            # handles the ace if total is greater than 21
            total += int(card['value'])
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total


"""
- This deal_cards function is to deal cards to player and dealer
- List manipulation is applied
- results are printed so that user knows they have been dealt

"""


def deal_cards(deck, nums_cards=2):
    # empty lists as hands
    player_hand = []
    dealer_hand = []
    for _ in range(nums_cards):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    #  print the dealers hand so that the user can see
    print("Dealer's hand:")
    for card in dealer_hand:
        print(f"{card['value']} of {card['suit']}")
    # print the players hand so that they know their values
    print("\nYour hand:")
    for card in player_hand:
        print(f"{card['value']} of {card['suit']}")
    # call dealers turn
    dealers_turn(deck, dealer_hand)
    return player_hand, dealer_hand


"""
- This is the dealers turn function
- While loop
- Appending the deck

"""


def dealers_turn(deck, dealer_hand):
    # if dealers hand is less than 17 dealer will hit
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    # calling players turn
    players_turn(deck, dealer_hand)
    return dealer_hand


"""
- This is the players turn function
- Adds an action input for hit or stand
- While loop
- Appending the deck

"""


def players_turn(deck, player_hand):
    while True:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print("\nYour hand: ")
            # a loop that iterates over each card in hand
            for card in player_hand:
                # uses a f-string to show value of card
                print(f"{card['value']} of {card['suit']}")
                # this calculates if players hand is greater than 21 = bust
            if calculate_hand(player_hand) > 21:
                print("You busted! Dealer wins.")
                return player_hand
                # if player selects "s" then current hand is held
        elif action == 's':
            return player_hand
            # this ensures a valid input is entered
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")


"""
- This calculates the winner using if/else statements

"""


def calculate_winner(player_hand, dealer_hand):
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    # if players hand is greater than 21 = dealer is winner
    if player_total > 21:
        return "dealer"
    # if dealers hand is greater than 21 = player is winner
    elif dealer_total > 21:
        return "player"
    # if totals are the same result = push/draw
    elif player_total == dealer_total:
        return "push"
    # if player total greater than dealer total = player
    elif player_total > dealer_total:
        return "player"
    # vice versa for dealer
    else:
        return "dealer"

# def show_winner():

# def play_again():


# main function to start game
def main():
    display_rules()
    # create the deck
    # create_deck()
    # calculate_hand()
    # deal_cards()
    # players_turn()


main()
