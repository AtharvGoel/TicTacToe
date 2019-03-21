import random
import sys

class Code:
	def tictactoe(self):
		print('\n   ' + list[0] + ' || ' + list[1] + ' || ' + list[2])
		print('   ======================')
		print('   ' + list[3] + ' || ' + list[4] + ' || ' + list[5])
		print('   ======================')
		print('   ' + list[6] + ' || ' + list[7] + " || " + list[8] + '\n')

		
	def playermove(self):
		pinput = input('Enter your move: ')
		
		if pinput == list[0]:
			list[0] = 'X '
		elif pinput == list[1]:
			list[1] = 'X '
		elif pinput == list[2]:
			list[2] = 'X '
		elif pinput == list[3]:
			list[3] = 'X '
		elif pinput == list[4]:
			list[4] = 'X '
		elif pinput == list[5]:
			list[5] = 'X '
		elif pinput == list[6]:
			list[6] = 'X '
		elif pinput == list[7]:
			list[7] = 'X '
		elif pinput == list[8]:
			list[8] = 'X '
		else:
			print('Please enter a valid move')
			y.playermove()
			
		y.tictactoe()
		
	def compmove(self):
		global player, list, c, p, move
		pinput = ' '

		for i in list:
			x = list.index(i)
			
			# Check for winning move
			if c == 'Computer Wins!':
				pinput = list[x]
			# block opponent's winning move
			elif p == 'You Win!':
				pinput = list[x]
			# play centre
			elif list[4] == '1,1':
				pinput = list[4]
			# play corner
			elif list[0] == '0,0' or list[2] == '0,2' or list[6] == '2,0' or list[8] == '2,2':  ### Check this statement
				if list[0] == '0,0':
					pinput = list[0]
				elif list[2] == '0,2':
					pinput = list[2]
				elif list[6] == '2,0':
					pinput = list[6]
				else:
					pinput = list[8]
			# Any random move
			else:
				pinput = list[random.choice([1,3,5,7])]
#				if list[1] == '0,1':
#					pinput = '0,1'
#				elif list[3] == '1,0':
#					pinput = '1,0'
#				elif list[5] == '1,2':
#					pinput = '1,2'
#				elif list[7] == '2,1':
#					pinput = '2,1'
#				else:
#					y.compmove()
			
		if pinput == 'X ':
			pinput = ' '
			y.compmove()
		elif pinput == 'O ':
			pinput = ' '
			y.compmove()
		else:
			pass
		
		if pinput == list[0]:
			move = list[0]
			list[0] = 'O '
		elif pinput == list[1]:
			move = list[1]
			list[1] = 'O '
		elif pinput == list[2]:
			move = list[2]
			list[2] = 'O '
		elif pinput == list[3]:
			move = list[3]
			list[3] = 'O '
		elif pinput == list[4]:
			move = list[4]
			list[4] = 'O '
		elif pinput == list[5]:
			move = list[5]
			list[5] = 'O '
		elif pinput == list[6]:
			move = list[6]
			list[6] = 'O '
		elif pinput == list[7]:
			move = list[7]
			list[7] = 'O '
		elif pinput == list[8]:
			move = list[8]
			list[8] = 'O '
		else:
			y.compmove()
			
		if pinput == 'X ':
			pinput = ' '
			y.compmove()
		elif pinput == 'O ':
			pinput = ' '
			y.compmove
		else:
			pass
			
	def checkp(player):
		global list, x
		if list[0]==list[1] and list[1]==list[2]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[3]==list[4] and list[4]==list[5]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[6]==list[7] and list[7]==list[8]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[0]==list[3] and list[3]==list[6]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[1]==list[4] and list[4]==list[7]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[2]==list[5] and list[5]==list[8]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[0]==list[4] and list[4]==list[8]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[2]==list[4] and list[4]==list[6]:
			p = 'You Win!'
			print('You Win!')
			y.tictactoe()
			sys.exit(0)
			
		else:
			pass
			
	def checkc(self):
		if list[0]==list[1] and list[1]==list[2]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[3]==list[4] and list[4]==list[5]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[6]==list[7] and list[7]==list[8]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[0]==list[3] and list[3]==list[6]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[1]==list[4] and list[4]==list[7]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[2]==list[5] and list[5]==list[8]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[0]==list[4] and list[4]==list[8]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		elif list[2]==list[4] and list[4]==list[6]:
			c = 'Computer Wins!'
			print('Computer Wins!')
			y.tictactoe()
			sys.exit(0)
			
		else:
			pass
			
y = Code()

list = ['0,0', '0,1', '0,2', '1,0','1,1','1,2','2,0','2,1','2,2']

print('Welcome to TicTacToe!')
player = 'X'
comp = 'O'

w = random.choice([player, comp])
print('\nYou are ' + player + ' and Computer is ' + comp + '\n')
gamePlay = True
c = ' '
p = ' '
z = 9

if w == player:
	print('\nYou start.\n')
else:
	print('\nComputer starts.\n')
while z > 0:
	while gamePlay == True:

		y.tictactoe()
				
		if w == player:
			y.playermove()
			y.checkp()
			if gamePlay == False:
				sys.exit(0)
			w = comp
		else:
			y.compmove()
			print('Computer plays: ' + move)
			y.checkc()
			w = player
		z -=1
