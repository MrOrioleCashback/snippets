"""
3/4/16
Coursera, An Introduction to Interactive Programming in Python (Part 2), Rice University
Mini-project #6 - 'Blackjack'
"""

import simplegui, random


CARD_SIZE, CARD_CENTER = (72, 96), (36, 48)
CARD_BACK_SIZE, CARD_BACK_CENTER = (72, 96), (36, 48)

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

score = 0
in_play = False


class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.rank + self.suit 

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Hand:
    def __init__(self):
        self.holding = []

    def __str__(self):
        hand = ''
        for card in self.holding:
            hand += str(card) + ' '
        return 'Hand contains %s' % str(hand)    

    def add_card(self, card):
        self.holding.append(card)

    def get_value(self):
        value, flag = 0, False
        for card in self.holding:
            value += VALUES[card.rank]
            if card.rank == 'A':
                flag = True
        return value + 10 if flag and value <= 11 else value
   
    def draw(self, canvas, pos):
        for index, card in enumerate(self.holding):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + CARD_SIZE[0] * index, pos[1] + CARD_CENTER[1]], CARD_SIZE)
        

class Deck:
    def __init__(self):
        self.card_deck = [Card(x, y) for x in SUITS for y in RANKS]

    def shuffle(self):
        random.shuffle(self.card_deck)

    def deal_card(self):
        return self.card_deck.pop()
    
    def __str__(self):
        cards = ''
        for card in self.card_deck:
            cards += str(card)+ ' '
        return 'Deck contains %s' % cards   


def deal():        
    global outcome, in_play, player_hand, dealer_hand, game_deck, down_card, outcome, score, prompt
    if in_play:
        score -= 1
    game_deck = Deck()
    game_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_card()), player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    in_play, down_card = True, True
    outcome = 'Hit or Stand?'
    prompt = ''
    
def hit():
    global in_play, outcome, score, prompt
    if player_hand.get_value() <= 21 and in_play:
        player_hand.add_card(game_deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = 'You busted!'
            prompt = 'New Deal?'
            in_play = False
            score -= 1
    
def stand():
    global in_play, down_card, outcome, score, prompt
    if in_play:
        down_card = False
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
        if dealer_hand.get_value() > 21 or player_hand.get_value() > dealer_hand.get_value():
            outcome = 'You win!'
            prompt = 'New Deal?'
            in_play = False
            score += 1
        else:
            outcome =  'You lose!'
            prompt = 'New Deal?'
            in_play = False 
            score -= 1
 
def draw(canvas):
    global player_hand, down_card, outcome, score, prompt
    canvas.draw_image(background,(1136/2, 640/2), (1136, 640), (800/2, 640/2), (800, 640))
    player_hand.draw(canvas, [200, 400])
    if down_card:
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_SIZE, (220, 230), CARD_SIZE)
    dealer_hand.draw(canvas, [200, 200])
    
    canvas.draw_text(str('Total: %s' % player_hand.get_value()), (20, 455), 40, 'Red')
    canvas.draw_text(str('Total: %s' % dealer_hand.get_value()), (20, 255), 40, 'Red')
    canvas.draw_text(outcome, (270, 100), 50, 'Yellow')
    canvas.draw_text(prompt, (270, 580), 50, 'Yellow')
    canvas.draw_polygon([[20, 20], [20, 100], [200, 100], [200, 20]], 5, 'Black', 'White')
    canvas.draw_text('Blackjack', (30, 75), 40, 'Black')
    canvas.draw_polygon([[600, 20], [600, 100], [780, 100], [780, 20]], 5, 'Black', 'White')
    canvas.draw_text('Score: %s' % score, (609, 76), 40, 'Black')

card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")  
background = simplegui.load_image("https://dl.dropbox.com/s/u0kz2mgqqqe772e/tableBackground.jpg?dl=1")
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
frame = simplegui.create_frame("Blackjack", 800, 640)
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.set_canvas_background("Green")

deal()
frame.start()