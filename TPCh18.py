class Card(object):
	"""docstring for Card"""
	def __init__(self, rank, suit):
		super(Card, self).__init__()
		self.rank = rank
		self.suit = suit

	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
		
	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

	def __lt__(self, other):
		"""suit is more important than rank in this instance so it is 
		first in a tuple comparison"""
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return t1 < t2



card1 = Card(2, 1)
print(card1) #=> 2 of Diamonds

"""compare cards with '<' and '>' using '__lt__' ('less than')
"""

card2 = Card(2, 3)
card3 = Card(3, 1)
print(card2) #=> 2 of Spades
print(card3) #=> 3 of Diamonds
print(card2 < card1) #=> False
print(card1 < card3) #=> True


import random


class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(rank, suit)
				self.cards.append(card)

	def __str__(self):
		result = []
		for card in self.cards:
			result.append(str(card))
		return '\n'.join(result)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def move_cards(self, hand, quantity):
		for i in range(quantity):
			hand.add_card(self.pop_card())


deck = Deck()
print(deck)
    #=> Ace of Clubs
    #=> 2 of Clubs
    #=> 3 of Clubs
    #=> ...
    #=> Jack of Spades
    #=> Queen of Spades
    #=> King of Spades

print('----------shuffle--------')
deck.shuffle()
print(deck)
    #=> King of Clubs
    #=> 4 of Hearts
    #=> Ace of Clubs
    #=> ...
    #=> 9 of Spades
    #=> 2 of Clubs
    #=> Jack of Spades

print('------------sort----------')
deck.sort()
print(deck)
    #=> Ace of Clubs
    #=> 2 of Clubs
    #=> 3 of Clubs
    #=> ...
    #=> Jack of Spades
    #=> Queen of Spades
    #=> King of Spades

"""Inheritance
"""

class Hand(Deck):
	"""docstring for Hand"""
	def __init__(self, label = ''):
		super(Hand, self).__init__()
		self.cards = []
		self.label = label


hand = Hand('New Hand')
print(hand.cards) #=> []
print(hand.label) #=> New Hand

print('---put a card in the hand---')
deck.shuffle()
hand.add_card(deck.pop_card())
print(hand) #=> Queen of Clubs

"""Lets make dealing cards eaiser by adding a 'move_cards' method, this 
will let us move a card from whomever calls the method to another hand, 
in some games cards move from deck to hand, or from hand to hand
"""

print('-----move cards-----')
hand.move_cards(deck, 1)
print(hand) #=> 
deck.move_cards(hand, 5)
print(hand)
    #=> Queen of Clubs
    #=> King of Clubs
    #=> 6 of Diamonds
    #=> King of Diamonds
    #=> 9 of Hearts

"""Queen of Clubs returns to the hand because it was appended to the end of 
the deck and returned when the deck popped a card.
"""

"""---Debugging---"""

"""Inheritance can make debugging difficult as you might lose track of where
a method resides, you can track where a method is called from by adding print
statements to methods, or...
"""

def find_defining_class(obj, method):
	for ty in type(obj).mro():
		if method in ty.__dict__:
			return ty

hand = Hand()
print(find_defining_class(hand, 'shuffle')) #=> <class '__main__.Deck'>

"""so the shuffle method is in the Deck class, find_defining_class uses the
mro method to get the list of class objects(type) that will be searched for
methods. mro stands for 'Method Resolution Order'
"""

"""When overriding a method stick to the principal that the interface of the 
new method is the same as the old method, same parameters, same output type, 
obey the same pre and post conditions, this is the Liskov Substitution Principle: 
a concept in Object Oriented Programming that states: Functions that use pointers 
or references to base classes must be able to use objects of derived classes 
without knowing it.
"""