import random
import sys

#list = ['0,0', '0,1', '0,2', '1,0','1,1','1,2','2,0','2,1','2,2']
a = '0,0'
b = '0,1'
c = '0,2'
d = '1,0'
e = '1,1'
f = '1,2'
g = '2,0'
h = '2,1'
i = '2,2'

def tictactoe():
	print('\n   ' + a + ' || ' + b + ' || ' + c)
	print('   ======================')
	print('   ' + d + ' || ' + e + ' || ' + f)
	print('   ======================')
	print('   ' + g + ' || ' + h + " || " + i + '\n')

user1 = input('\nEnter Player\'s name: ')
user2 = input('Enter Player\'s name: ')

start = random.choice([user1, user2])
if start == user2:
	user1, user2 = user2,user1
print('\n' + user1 + ' wins toss.')
tictactoe()
dict = {'X':user1, 'O':user2}

def winX():
	if a==b and b==c:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif d==e and e==f:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif g==h and h==i:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif a==d and d==g:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif b==e and e==h:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif c==f and f==i:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif a==e and e==i:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	elif c==e and e==g:
		print(dict['X'] + ' wins!')
		sys.exit(0)
	else:
		pass

def winO():
	if a==b and b==c:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif d==e and e==f:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif g==h and h==i:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif a==d and d==g:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif b==e and e==h:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif c==f and f==i:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif a==e and e==i:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	elif c==e and e==g:
		print(dict['O'] + ' wins!')
		sys.exit(0)
	else:
		pass

z = 9
while z > 0:
	user_input = input(user1 + ', What\'s your move: ')
	z-=1
	def gameX():
		global a, b, c, d, e, f, g, h, i, user_input
		if a == user_input :
			a = 'X  '
		elif b == user_input:
			b = 'X  '
		elif c == user_input:
			c = 'X  '
		elif d == user_input:
			d = 'X  '
		elif e == user_input:
			e = "X  "
		elif f == user_input:
			f = 'X  '
		elif g == user_input:
			g = 'X  '
		elif h == user_input:
			h = 'X  '
		elif i == user_input:
			i = 'X  '
		else:
			print('Please enter a valid move')
			user_input = input(user1 + ', What\'s your move: ')
			gameX()
		winX()
	gameX()
	tictactoe()
	

	user_input = input(user2 + ', enter your move: ')

	def gameO():
		global a, b, c, d, e, f, g, h, i, user_input
		if a == user_input :
			a = 'O  '
		elif b == user_input:
			b = 'O  '
		elif c == user_input:
			c = 'O  '
		elif d == user_input:
			d = 'O  '
		elif e == user_input:
			e = "O  "
		elif f == user_input:
			f = 'O  '
		elif g == user_input:
			g = 'O  '
		elif h == user_input:
			h = 'O  '
		elif i == user_input:
			i = 'O  '
		else:
			print('Please enter a valid move')
			user_input = input(user2 + ', what\'s your move: ')
			gameO()
		winO()
	gameO()
	tictactoe()

input('Press Enter to continue ')
sys.exit(0)