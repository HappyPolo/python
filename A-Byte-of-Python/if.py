#!/usr/bin/python
# Filenname : if.py

number =23
guess = int (input('Enter an integer : ')) # raw_input 3.5之后不支持
if guess == number:
	print ('Congratulations,you guessed it.')
	print ('but you do not win any prizes!')
elif guess < number:
	print ('No,it is little higher than that!')
else:
	print ('No,it is little lower than that!')
print("Done")
