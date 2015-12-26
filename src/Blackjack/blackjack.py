from random import shuffle
from random import randint

"""

Very basic implementation of the game Blackjack.

One player vs. The Dealer

Player can only "Hit" and "Stay" as of now

Dealer makes random moves.

"""

class Player(object):

	"""

	Player class that provides various convenient and useful methods and fields

	"""

	def __init__(self):

		"""
		Initialize the Players values such as his cards, moves, total etc.

		"""

		self.currentTotal = 0 # Sum total of the players' cards
		self.moves = [] # List of all the moves made by the player
		self.cards = [] # List of all the players' cards
		self.busted = False # Whether or not the player got busted
		self.dealerOrNot = False # Whether or not the player is the dealer.

	def addCard(self,n):

		"""
		Adds a card to the player's deck and updates his total score

		"""
		self.cards.append(n)

		self.updateTotal()

	def removeCard(self,n):
		"""
		Removes a card from the player's deck

		Returns False if the card isn't in the deck. Otherwise removes the card and returns True
		"""
		if(n in self.cards): # Checks if the card is even in the players deck

			self.cards.remove(n)
			self.updateTotal()

			return True

		return False

	def updateTotal(self):

		"""
		Updates the total score of the player (Sum of the values of his cards)
		"""

		a = [] # List that contains numerical values of all the players' cards. (EG: Jack has a value of 11)

		for b in self.cards: # Adding all the cards to 'a'

			if(b[0] < 11): # if a number card, add its face value

				a.append(b[0])

			elif(b[0] >= 11 and b[0] != 14): # if a face card (but not an Ace) add 10

				a.append(10)

			else: # if an Ace, add 1 or 11 depending on which will NOT bust the player

				if(self.currentTotal + 11) > 21:

					a.append(1)

				else:

					a.append(11)

		self.currentTotal = sum(a) # Updating the total to be the sum of all the values

	def fixLastCardVal(self):

		"""
		In case player gets 21 on initial cards. Would make game boring. Hence, fix by a margin
		"""

		self.cards[len(self.cards) - 1][0] -= randint(1,8) # Reducing the value of the last card by a random value from 1 to 8
		self.updateTotal()

	def makeDealer(self):

		"""
		Makes the player the Dealer.

		"""
		self.dealerOrNot = True


	def addMove(self, move):

		"""
		Add a move to the list of moves by the Player
		"""

		self.moves.append(move)

	def bust(self):

		"""
		Set the players' status to busted (Gone over 21)
		"""

		self.busted = True

	def isBusted(self):

		"""
		returns: Boolean

		Whether or not the player is busted.
		"""

		return self.busted

	def getTotal(self):

		"""
		returns: int
		Total sum value of all the players' cards
		"""

		return self.currentTotal

	def nMoves(self):

		"""
		returns: int
		returns the number of moves made by the player
		"""

		return len(self.moves)

	def nCards(self):

		"""
		returns: int
		Returns the number of cards the player currently has
		"""

		return len(self.cards)

	def getCards(self):

		"""
		returns: List of integers

		Returns the players entire deck as a list
		"""

		return self.cards

	def isDealer(self):

		"""
		returns: Boolean

		Returns whether or not the player is the dealer.
		"""

		return self.dealerOrNot

	def getLastCard(self):

		"""
		returns: int

		Returns the last card in the players' deck
		"""

		return self.cards[(len(self.cards) - 1)]



def createDeck(n):

	"""
	#11 --> Jack
	#12 --> Queen
	#13 --> king
	#14 --> Ace

	Value of all < 11 are their face Value

	Value for rest is 10

	Ace (14) can have a value of 1 or 11

	n is number of decks to be added in

	"""

	kingdoms = ["clubs", "diamonds", "hearts", "spades"] # List of kingdoms in a deck of cards

	deck = [] # The deck to be used

	for b in xrange(n): # Adding 'n' decks

		for i in xrange(len(kingdoms)): # Add cards for each deck

			for j in xrange(2,15):

				a = [j, kingdoms[i]]
				deck.append(a)

	for i in xrange(100): # Shuffling the deck 100 times
		shuffle(deck)

	return deck

def checkPlayer(player):

	"""
	Args --> player, a Player object
	Checks whether the player has gone over 21, or has gotten a score of 21 or is currently safe

	Returns: string
	"""

	total = player.getTotal()

	if(total > 21):

		player.bust() # Bust the player
		return "busted"

	elif(total == 21):

		return "won"

	else:

		return "safe"

def displayCards(player):

	"""
	Args --> player, a Player object

	Displays all of the players' cards in the format "card of kingdom"
	"""
	st = ""

	for a in player.getCards(): # Going over each card

		if(a[0] < 11): # If it's a numerical card
			st += str(a[0]) + " of " + a[1] + ", "  # a[0] is the number of the card, a[1] is the kingdom

		elif(a[0] >= 11 and a[0] != 14): # If face card but not an Ace

			if(a[0] == 11): # if it is a Jack
				x = "Jack"

			elif(a[0] == 12): # if it is a Queen
				x = "Queen"

			elif(a[0] == 13): # if it is a King
				x = "King"

			st += x + " of " + a[1] + ", "

		else: # it's an Ace
			st += "Ace" + " of " + a[1] + ", "

	return st

def makeMove(move, playa, dec, initOrNot):

	if(move in [1,2]):

		if move == 1:

			playa.addCard(dec.pop()) # Give the player a card from the deck


			if(initOrNot == False): # Check if this is being done during initialization. (Don't wanna do that)

				playa.addMove("HIT") # Add the move to the players list of moves

				if(playa.isDealer() == False): # Check if the player is the Dealer

					print "You hit. You got a " + str(playa.getLastCard())
					print ""

				else:
					print "The dealer hit. He got a " + str(playa.getLastCard())
					print ""

		else:

			if(initOrNot == False): # Check if this is being done during initialization. (Don't wanna do that)

				playa.addMove("STAY")

				if(playa.isDealer() == False): # Check if the player is the Dealer
					print "You stayed"
					print ""

				else:
					print "The dealer stayed"
					print ""

		for i in xrange(100): # Shuffle the deck 100 times. (To maintain randomness of cards)
			shuffle(dec)

		valid = checkPlayer(playa) # Check if the player busted, won or is safe



		if(valid == "busted"): # Player or Dealer busted

			total = playa.getTotal() # Total value of the player

			if(playa.isDealer() == False): # Player is not dealer

				print "I'm sorry. You busted."

				print "You have a total of " + str(total)

				print "Your cards were:"

				print displayCards(playa)

				print "Bye. Better luck next time"

			else:

				print "Congrats! You won! The dealer busted!"
				print "The dealer had a total of " + str(total)
				print ""
				print "The dealer's cards were: "
				print displayCards(playa)

			return False

		elif(valid == "won"): # Player or Dealer has won

			if(initOrNot == True): # Don't want someone to win before the game starts

				playa.fixLastCardVal() # Adjust their cards if that happens


			if(playa.isDealer() == False): # Check if player is a dealer

				print "Congrats! You won! You got a total of 21!"

				print "Your cards were: "

				print displayCards(playa)

				print ""

				print "Thanks for playing! Bye!"

			else:

				print "I'm sorry, you lost. The dealer reached 21 before you."
				print "Better luck next time."

				print "The dealers cards were:"
				print ""
				print displayCards(playa)

			return False

		else: # Player or Dealer is safe

			if(initOrNot == False):

				if(playa.isDealer() == False):

					print "Your cards are: "
					print displayCards(playa)
					print ""
					print "Your total is " + str(playa.getTotal())

				else:

					print "The dealers cards are: "
					print displayCards(playa)
					print ""
					print "The dealers total is " + str(playa.getTotal())

			return True


	else:
		raise

def init(players, deck): # Initialize each players' deck

	for player in players:

		for i in xrange(2):

			makeMove(1, player, deck, True)

def main():

	welcomeString = """ Welcome to (modest) Blackjack! Your objective is to get to a total of 21

				* If the total sum of your cards goes over 21, you lose
				* If the dealer reaches 21 before you, you lose
				* If the dealer goes over 21 before you, you win

				* You can "Hit": Get a card (Do this by entering 1)
				* You can "Stay": Do nothing (Do this by entering 2)

				Good luck!

					"""

	deck = createDeck(1) # Initialize our deck
	dealer = Player() # Create a dealer
	dealer.makeDealer() # make it a dealer
	ourPlayer = Player() # Make ourplayer

	init([ourPlayer, dealer], deck) # Initialize the players

	print welcomeString
	print ""

	print "Your cards are: "
	print displayCards(ourPlayer)
	print ""
	print "Your total is " + str(ourPlayer.getTotal())

	print ""
	print ""

	print "The Dealers cards are: "
	print displayCards(dealer)
	print ""
	print "The Dealers total is " + str(dealer.getTotal())

	print ""
	print ""

	while True:

		move = -1 # Invalid initial value (on purpose)

		while True:
			mov = raw_input("Please enter your move. 1 for Hit. 2 for Stay. ").strip() # Getting move from player  .strip() removes trailing and leading spaces

			if(mov == "1" or mov == "2"): # Checking if the move is valid

				move = int(mov)
				break

			else: # Invalid input
				print "Incorrect input, try again"
				print ""

		exi = makeMove(move, ourPlayer, deck, False)

		if exi == False: # Player has won/lost

			break

		dealerMove = randint(1,2) # make a random move on part of the dealer

		exi = makeMove(dealerMove, dealer, deck, False)

		if exi == False: # Dealer has won/lost

			break

if __name__ == '__main__':
	main()
