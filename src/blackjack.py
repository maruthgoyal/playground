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
		
		self.currentTotal = 0
		self.moves = []
		self.cards = []
		self.busted = False
		self.dealerOrNot = False

	def addCard(self,n):

		"""
		Adds a card to the player's deck and updates his total score

		"""
		self.cards.append(n)

		self.updateTotal()

	def removeCard(self,n):
		"""
		Removes a card from the player's deck
		"""
		if(n in self.cards):

			self.cards.remove(n)
			self.updateTotal()

			return True

		return False

	def updateTotal(self):

		"""
		Updates the total score of the player (Sum of the values of his cards)
		"""

		a = []

		for b in self.cards:

			if(b[0] < 11):

				a.append(b[0])

			elif(b[0] >= 11 and b[0] != 14):

				a.append(10)

			else:

				if(self.currentTotal + 11) > 21:

					a.append(1)

				else:

					a.append(11)

		self.currentTotal = sum(a)

	def fixLastCardVal(self):

		"""
		In case player gets 21 on initial cards. Would make game boring. Hence, fix by a margin
		"""

		self.cards[len(self.cards) - 1][0] -= randint(1,8) 
		self.updateTotal()

	def makeDealer(self):
		self.dealerOrNot = True


	def addMove(self, move):

		self.moves.append(move)

	def bust(self):

		self.busted = True

	def isBusted(self):

		return self.busted

	def getTotal(self):

		return self.currentTotal

	def nMoves(self):

		return len(self.moves)

	def nCards(self):

		return len(self.cards)

	def getCards(self):

		return self.cards

	def isDealer(self):

		return self.dealerOrNot

	def getLastCard(self):

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

	kingdoms = ["clubs", "diamonds", "hearts", "spades"]

	deck = []

	for b in xrange(n):

		for i in xrange(len(kingdoms)):

			for j in xrange(2,15):

				a = [j, kingdoms[i]]
				deck.append(a)

	for i in xrange(30):
		shuffle(deck)

	return deck

def checkPlayer(player):
	
	total = player.getTotal()
	
	if(total > 21):

		player.bust()
		return "busted"

	elif(total == 21):

		return "won"

	else:

		return "safe"

def displayCards(player):
	st = ""

	for a in player.getCards():

		if(a[0] < 11):
			st += str(a[0]) + " of " + a[1] + ", "

		elif(a[0] >= 11 and a[0] != 14):

			if(a[0] == 11):
				x = "Jack"

			elif(a[0] == 12):
				x = "Queen"

			elif(a[0] == 13):
				x = "King"

			st += x + " of " + a[1] + ", "

		else:
			st += "Ace" + " of " + a[1] + ", "

	return st

def makeMove(move, playa, dec, initOrNot):

	if(move in [1,2]):

		if move == 1:

			playa.addCard(dec.pop())


			if(initOrNot == False):
				
				playa.addMove("HIT")
				if(playa.isDealer() == False):

					print "You hit. You got a " + str(playa.getLastCard())
					print ""

				else:
					print "The dealer hit. He got a " + str(playa.getLastCard())
					print ""

		else:

			if(initOrNot == False):

				playa.addMove("STAY")

				if(playa.isDealer() == False):
					print "You stayed"
					print ""

				else:
					print "The dealer stayed"
					print ""

		shuffle(dec)
		
		valid = checkPlayer(playa)



		if(valid == "busted"):

			total = playa.getTotal()

			if(playa.isDealer() == False):

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

		elif(valid == "won"):

			if(initOrNot == True):

				playa.fixLastCardVal()


			if(playa.isDealer() == False):

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

		else:

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

def init(players, deck):

	for player in players:

		for i in xrange(2):

			makeMove(1, player, deck, True)



welcomeString = """ Welcome to (modest) Blackjack! Your objective is to get to a total of 21

			* If the total sum of your cards goes over 21, you lose
			* If the dealer reaches 21 before you, you lose
			* If the dealer goes over 21 before you, you win 

			* You can "Hit": Get a card (Do this by entering 1)
			* You can "Stay": Do nothing (Do this by entering 2)

			Good luck!

				"""

deck = createDeck(1)
dealer = Player()
dealer.makeDealer()
ourPlayer = Player()

init([ourPlayer, dealer], deck)

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

	move = -1

	while True:
		mov = raw_input("Please enter your move. 1 for Hit. 2 for Stay. ")
		
		if(mov == "1" or mov == "2"):
			
			move = int(mov)
			break

		else:
			print "Incorrect input, try again"
			print ""

	exi = makeMove(move, ourPlayer, deck, False)

	if exi == False:

		break

	dealerMove = randint(1,2)

	exi = makeMove(dealerMove, dealer, deck, False)

	if exi == False:

		break







