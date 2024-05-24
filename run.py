# import random for shuffling of cards
import random
# importing colorama to add colour to text
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


"""
- Display's the rules of the game to the user.
- The function uses primarily print statements.
- Gives information on card values, player actions of hit/stand
  and overall objective of the game.

"""


def display_rules():
    print(Style.BRIGHT + "WELCOME TO BLACK JACK!\n")
    print(Back.RED + "RULES: ")
    print("- To win and beat the dealer you need to get to 21 "
          "without going over.")
    print("- Card values of King, Queen, and Jack are worth 10.")
    print("- Ace can be worth either 1 or 11.")
    print("- Other cards are worth their presented number.")
    print("- Hit will grant you another card.")
    print("- Stand will keep your current hand.")
    print("- The dealer will hit until they reach 17 or higher.")
    print("- If you and the dealer tie, this is called a push "
          "and no one wins.\n")


"""
- A card game needs a deck so this creates the game deck.
- The function uses a list of dictionaries that represents
  each card in the deck
- Each card is represented with the value and suit i.e, 8 of Hearts
- Applies the random module for shuffling.
- Returns a shuffled list of dictionaires which is the deck

"""


def create_deck():
    values = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5',
              '4', '3', '2']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # making the 52 cards
    deck = [{'value': value, 'suit': suit}
            for value in values for suit in suits]
    # shuffles the deck
    random.shuffle(deck)
    return deck


"""
- Calculate hand function is to assess the total value of the hands dealt.
- Contains a while loop.
- Contains list iteration with for loop.
- Conditional statements for the ace calculations:
  if the hand contains aces and exceeds the value of 21,
  the function converts the ace from 11 to 1.

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
- As default only two cards are dealt
- List manipulation is applied
- Parameters are the deck and 2 cards to be dealt
- Results are return so that player knows they have been dealt

"""


def deal_cards(deck, nums_cards=2):
    # empty lists as hands
    player_hand = []
    dealer_hand = []
    for _ in range(nums_cards):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    #  print the dealers hand so that the user can see
    print(Fore.RED + "Dealer's hand 😅 ")
    for card in dealer_hand:
        print(f"{card['value']} of {card['suit']}")
    # print the players hand so that they know their values
    print(Fore.GREEN + "\nYour hand 🫣 ")
    for card in player_hand:
        print(f"{card['value']} of {card['suit']}")
    return player_hand, dealer_hand


"""
- This is the dealers turn function
- The dealer will draw cards until their value is at least 17
- While loop
- Appends the dealers hand
- Returns dealers hand

"""


def dealers_turn(deck, dealer_hand):
    # if dealers hand is less than 17 dealer will hit
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand


"""
- This is the players turn function
- Adds an action input for hit or stand
- The player is prompted until they stand or bust
- While loop
- Returns the players hand after drawing cards
- Parameters are:
  The deck to deal cards
  The players hand to see their current hand
  The dealers hand that is shown to player

"""


def players_turn(deck, player_hand, dealer_hand):
    while True:
        action = input(Fore.YELLOW + "\nDo you want to hit or stand? "
                       "(h/s) 🤨 ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print(Fore.GREEN + "\nYour hand 😳 ")
            # a loop that iterates over each card in hand
            for card in player_hand:
                # uses a f-string to show value of card
                print(f"{card['value']} of {card['suit']}")
                # this calculates if players hand is greater than 21 = bust
            if calculate_hand(player_hand) > 21:
                print(Fore.RED + "You busted! Dealer wins 😭 ")
                # returning the player hand even though they best
                return player_hand
                if not play_again():
                    print(Style.BRIGHT + "\nThanks for playing this "
                          "Black Jack Game! 🥰 ")
                    exit()
                # if player selects "s" then current hand is held
        elif action == 's':
            return player_hand
            # this ensures a valid input is entered
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand. 😇")


"""
- This calculates the winner using if/else statements based on hand values
- Does this by comparing dealers hand and players hand values
- Parameters used are:
  Player_hand - final hand
  Dealers_hand - final hand
- Returns the winner through a string that could be:
  Player, Dealer, or Push

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


"""
- Displays the winner of the game
- Shows dealers hand total and players hand total
- Then announces Winner or announces Draw
- Parameters:
  player hand for players final hand
  dealers hand for dealers final hand

"""


def show_winner(player_hand, dealer_hand):
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
# shows the dealers hand total
    print(Fore.RED + "\nDealer's hand 🤖 ")
    for card in dealer_hand:
        print(f"{card['value']} of {card['suit']}")
    print("Dealer's total: ", dealer_total)
# shows the player hands total
    print(Fore.GREEN + "\nYour hand 🤠 ")
    for card in player_hand:
        print(f"{card['value']} of {card['suit']}")
    print("Your total: ", player_total)
# Displays who the winner is
    winner = calculate_winner(player_hand, dealer_hand)
    if winner == "push":
        print(Fore.CYAN + "It's a push! Go again to get a winner! 😱 ")
    else:
        print(f"The winner is {winner.capitalize()}!")


"""
- Function to play again
- Asks if player wants to play again
- Returns a bool - True if play again - false if not
"""


def play_again():
    while True:
        again = input(Fore.CYAN + "\nDo you want to play again?"
                      "(y/n) 😎 ").lower()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no 😣 ")


"""
- Main function to start the game
- Initiates the game by displaying the rules
- Then enters a loop to play rounds of black jack until user decides otherwise

The flow of the game:
- Creates and shuffles deck
- Deals out cards to dealer and player
- Players turn = hit or stand
- If player does not bust
- Determines the winner and displays winner of round.
- Prompts player to play again
- The game ends when player doesn't want to play again

Error handling:
- If an exception occurs in the game, it is caught
  and a message is displayed:
  an error occurred and game will be restarted

"""


if __name__ == "__main__":
    display_rules()
    while True:
        try:
            deck = create_deck()
            player_hand, dealer_hand = deal_cards(deck)
            player_hand = players_turn(deck, player_hand, dealer_hand)
            if calculate_hand(player_hand) <= 21:
                dealer_hand = dealers_turn(deck, dealer_hand)
                show_winner(player_hand, dealer_hand)
            if not play_again():
                print(Style.BRIGHT + "\nThanks for playing this "
                      "Black Jack Game!")
                break
        except Exception as e:
            print(Fore.RED + f"OH NO! An error has occurred: {e}. "
                  "Restarting the Game! 🙀 ")
