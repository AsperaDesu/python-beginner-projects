import random

print('GUESS THE NUMBER')
print('=' * 16)

def lvl(user):
	return random.randint(1, user)
	
answer = lvl(int(input('Level : ')))

def checking(guess):
	try:
		if guess == answer: 
				print('Just right!')
				return True
		elif guess < answer:
				print('Too large!')
		else: 
				print('Too small!')
	
	except:
		print('Invalid Answer!')

guess = 0 

if not checking(guess):
	guess = int(input('Guess : '))
	checking(guess)
