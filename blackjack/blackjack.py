# Project - Blackjack
# Allows user to play blackjack against a computer dealer

import tkinter as tk
import random
import time

# Load card images using PIL

# initialize some useful global variables
game_in_progress = False
outcome = ''
score = 0

# define globals for cards
SUITS = ('clubs', 'spades', 'hearts', 'diamonds')
RANKS = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')
VALUES = {'ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}
PLAYER_POS = (250, 400)
DEALER_POS = (250, 100)


# define card class
class Card:
    def __init__(self, rank, suit):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.filename = 'cards\\' + rank + '_of_' + suit + '.gif'
            self.image = None
        else:
            self.suit = None
            self.rank = None
            self.filename = None
            self.image = None
            print("Invalid card:", suit, rank)

    def __repr__(self):
        return self.rank.upper() + ' of ' + self.suit.upper()

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_filename(self):
        return self.filename

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def draw(self, canvas, pos):
        # draw the card
        pass


# define hand class
class Hand:
    def __init__(self):
        self._cards = []

    def __str__(self):
        return str(self._cards)

    def add_card(self, card):
        self._cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ranks = []
        for i in range(len(self._cards)):
            value += VALUES[self._cards[i].get_rank()]
            ranks.append(self._cards[i].get_rank())
        if 'ace' in ranks and value <= 11:
            value += 10
        return value

    def draw(self, c, pos):
        global outcome, outcome_label, score, score_label
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self._cards)):
            canvas.delete(self._cards[i].get_image)
        faces = []
        for i in range(len(self._cards)):
            face = tk.PhotoImage(file=self._cards[i].get_filename())
            face = face.subsample(8,8)
            self._cards[i].set_image(face)
            canvas.create_image(pos[0] + (i*20), pos[1], image=face)
            canvas.pack()

        outcome_label.config(text='')
        score_label.config(text='Score: ' + str(score))


# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self._cards = []
        for rank in RANKS:
            for suit in SUITS:
                self._cards.append(Card(rank, suit))

    def shuffle(self):
        # shuffle the deck, using random.shuffle()
        random.shuffle(self._cards)

    def deal_card(self):
        # deal a card object from the deck
        return self._cards.pop()

    def __str__(self):
        # return a string representing the deck
        deck_str = ''
        for i in range(len(self._cards)):
            deck_str += str(self._cards[i]) + '\n'
        return deck_str


# define event handlers for buttons
def deal():
    # If game is in progress, player loses. Then, create and deal a hand to the player and dealer.
    global outcome, game_in_progress, score, canvas, outcome_label, score_label

    if game_in_progress:
        outcome = 'Player forfeits.'
        outcome_label.config(text=outcome)
        score -= 1

    canvas.delete('all')

    global deck
    deck = Deck()
    deck.shuffle()

    global player_hand, dealer_hand
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print(player_hand)
    player_hand.draw(canvas, PLAYER_POS)
    dealer_hand.draw(canvas, DEALER_POS)

    game_in_progress = True


def hit():
    # Add a card to the player's hand. If busted, the player loses.
    global player_hand, deck, outcome, score, game_in_progress, canvas, outcome_label
    if not game_in_progress:
        outcome = 'Illegal move! Please press "Deal."'
        outcome_label.config(text=outcome)
        return
    player_hand.add_card(deck.deal_card())
    player_hand.draw(canvas, PLAYER_POS)

    if player_hand.get_value() > 21:
        outcome = 'Player busts!'
        score -= 1
        outcome_label.config(text=outcome)
        score_label.config(text='Score: ' + str(score))
        game_in_progress = False


def stand():
    # Player decides to stop gaining cards. Dealer adds cards to dealer_hand as long as
    # its value is less than 17.
    global player_hand, dealer_hand, deck, outcome, score, game_in_progress, canvas, outcome_label
    if not game_in_progress:
        outcome = 'Illegal move! Please press "Deal."'
        outcome_label.config(text=outcome)
        return
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.draw(canvas, DEALER_POS)
        time.sleep(1)
    if dealer_hand.get_value() > 21:
        outcome = 'Dealer busts! Player wins.'
        score += 1
    elif dealer_hand.get_value() > player_hand.get_value():
        outcome = 'Dealer wins! Player loses.'
        score -= 1
    elif dealer_hand.get_value() == player_hand.get_value():
        outcome = 'Tie! Dealer wins.'
        score -= 1
    elif player_hand.get_value() == 21:
        outcome = 'Blackjack! Player wins!'
        score += 1
    elif dealer_hand.get_value() < player_hand.get_value():
        outcome = 'Player wins!'
        score += 1
    outcome_label.config(text=outcome)
    score_label.config(text='Score: ' + str(score))
    game_in_progress = False


# draw handler
# def draw(canvas):
#     # test to make sure that card.draw works, replace with your code below
#
#     card = Card('ace', 'spades')
#     card.draw(canvas, [300, 300])


# build the GUI
## TODO: Add labels for player and dealer
## TODO: (optional) Make one of the dealer cards unknown
root = tk.Tk()
root.title('Blackjack')
frame = tk.Frame(root)
frame.pack()

button_frame = tk.Frame(frame)
button_frame.grid(row=0, column=0, sticky=tk.N)
deal_button = tk.Button(button_frame, text='Deal', width=10, command=deal)
hit_button = tk.Button(button_frame, text='Hit', width=10, command=hit)
stand_button = tk.Button(button_frame, text='Stand', width=10, command=stand)
# game_status = tk.

deal_button.grid(column=0, row=0, sticky=tk.W, padx=50)
hit_button.grid(column=0, row=1, sticky=tk.W, padx=50)
stand_button.grid(column=0, row=2, sticky=tk.W, padx=50)


outcome_label = tk.Label(button_frame, pady=30, text='Welcome!')

score_label = tk.Label(button_frame, pady=30, text='Score: 0')

outcome_label.grid(column=0, row=4)
score_label.grid(column=0, row=6)

canvas_frame = tk.Frame(frame)
canvas_frame.grid(row=0, column=1)

canvas = tk.Canvas(canvas_frame, background='green', height=500, width=500)
canvas.pack(side=tk.RIGHT)

# starts the game
root.mainloop()
