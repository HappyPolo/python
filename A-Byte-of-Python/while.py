#!/usr/bin/python
# Filename : while.py

number =23
running =True

while running:
	guess = int (raw_input('Enter an integer : '))

	if guess == number:
		print ('Congratulations,you guessed it.')
		running = False
	elif guess < number:
		print ('No,it is little higher than that!')
	else :
		print ('No,it is little lower than that!')

print ('Done')