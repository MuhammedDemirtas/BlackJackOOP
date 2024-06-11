# BlackJackOOP

This project simulates the classic Blackjack game where the player and the dealer aim to get as close to 21 as possible without exceeding it. The player draws cards or stands to reach 21, while the dealer must draw cards until reaching 17. The Ace can be valued at either 1 or 11, and if the total card values exceed 21, the player or dealer goes "bust" and loses the game.

-----------------------------------------------------------

# Classes and Functions

* Card Class (Card)
* Purpose: To create and define cards for the deck.

* Attributes:

* suit (color): Hearts, Diamonds, Clubs, Spades.
* rank: Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace.
* Methods:

* __str__: Provides a string representation of the cards.
* Deck Class (Deck)
* Purpose: To create a deck of 52 cards.

* Attributes

* deck: List of cards.
* Methods

* __init__: Initializes a deck of 52 cards.
* __str__: Prints the entire deck.
* shuffle: Shuffles the deck.
* deal_card: Draws a card from the deck and returns it.
* Hand Class (Hand)
* Purpose: Represents the hands of the player and the dealer.

* Attributes:

* hand: List of cards.
* value: Total value of the hand.
* aces: Number of aces in the hand.

* Methods

* add_card: Adds a card to the hand and updates the value.
* adjust_for_ace: Adjusts the value of aces in the hand to prevent busting.
* Chips Class (Chips)
* Purpose: Manages the player's bets and total chips.

* Attributes

* total: Total chips the player has.
* bet: The player's bet for the round.
* Methods:

* win_bet: Increases the total chips when the player wins a bet.
* lose_bet: Decreases the total chips when the player loses a bet.
* Functions
* take_bet: Takes the bet value from the player.
* hit: Draws a card from the deck and adds it to the hand.
* hit_or_stand: Asks the player whether to hit or stand.
* show_some: Shows some of the cards, hiding the dealer's first card.
* show_all: Shows all cards and their values.
* player_busts: Executes actions when the player busts.
* player_wins: Executes actions when the player wins.
* dealer_busts: Executes actions when the dealer busts.
* dealer_wins: Executes actions when the dealer wins.
* push: Executes actions when there's a tie.

----------------------------------------------

# Game Flow

* Introduction: The player is greeted with a welcome message and the rules of the game are explained.

* Deck Creation: A new deck is created and shuffled.

* Hand Creation: Both the player and the dealer are dealt two cards each.

* Betting: The player is asked to place a bet.

* Show Initial Cards: Some cards are shown, with one of the dealer's cards hidden.

* Hit or Stand: The player decides whether to hit or stand.

---------------------------------------------------

# Game Result

* If the player busts, the game ends.
* If the player does not bust, the dealer draws cards and the result is evaluated.
* Chips Update: The player's total chips are updated based on the game result.
* Replay: The player is asked if they want to play again.
* Running the Game
* To run the game, you need to have Python installed. Run the code to start the game. You can replay the game by pressing e or end the game by pressing h.

-----------------------------------------------------

# Requirements

* Python 3.x

--------------------------------------

# How to Run?
* Ensure Python 3.x is installed.
* Paste the code into a Python file (e.g., blackjack.py).
* Run the file from the terminal or command line: python blackjack.py
* Follow the on-screen instructions to play the game.
* Enjoy the game!
