# BLACK JACK: LEVEL 1

This is the classic and highly popular casino black jack game but stripped down to its basic functions hence the name, "Black Jack: Level 1". It excludes the premise of betting and simply allows the player to hit or stand in order to beat the dealer.
![screenshot of heroku deployment](./images/screenshots.png)
You can access the game on heroku via this link:

- https://black-jack-lvl1-25fdd631e5ae.herokuapp.com/

## HOW TO PLAY

How to play is set out in the rules:
![screenshot of heroku deployment](./images/heroku-deployed.png)

Following the guidelines set out by, "https://www.blackjackapprenticeship.com/how-to-play-blackjack/" with a few omissions of:

- Wagering
- Betting
- Doubling Down
- Splitting

## FEATURES

The features follow this balsamiq flowchart:
![balsamiq flowchart](./images/balsamiq-flowchart.png)

### EXISTING FEATURES

The existing features are as follows:

1. Random deck creation:

- A new shuffled deck is created upon every round

2. Play against computer:

- You play against the dealer who hits until its hand reaches 17

3. Accepts user input:

- Opting to hit or stand
- Opting to play again

4. Maintains value of cards dealt:

- The game knows the total value of the cards that it uses when determining the winner

5. Input validation and error handling:

- The game ensures you have entered the correct values when hitting (h) or standing (s)
- The games does the same for play again values with (y) and (n)

### FUTURE FEATURES

Future features will ensure that the Black Jack game is played at its casino level that includes all of the standard features you would aexpect to see when playing at a casino in Las Vegas:

- Wagering
- Betting
- Doubling Down
- Splitting

As well as:

- Choosing amount of rounds
- How many players
- Total winnings and loses

## TESTING

### BUGS

#### SOLVED BUGS

1. Returning "BUSTED" as a string in the players turn:

- Caused a type error because it changed the expected return type of the function. The code expected the players_turn to return a list of cards (the player's hand) rather than string.

2. When busted and player plays again - hands are not displayed:

- This was due to the fact that return player's hand was missing, as this ensures hands are displayed.

### REMAINING BUGS

- No remaining bugs

### VALIDATOR TESTING

I installed FLAKE8 which adheres to pep8 stands which states: "no problems"

### DEPLOYMENT

This project was deployed using code institutes python template from github for gitpod and then onto Heroku.

#### Steps for deployment:

- Fork/clone the repository from my github: https://github.com/Ojay97-hub/black-jack-game
- Go to heroku and create new app
- Set buildbacks in order of Python and NodeJS
- Link Heroku app to github repository
- Click on deploy

### CREDITS

- Code institute for the python template
- https://www.blackjackapprenticeship.com/how-to-play-blackjack/
