#! /usr/bin/python3

number = 23
running = True

while running:
    guess = int(raw_input('  Enter an Integer : '))

    if guess == number:
        print ('Congratulations')
        ruuning = False
    elif guess < number:
        print("  No")
    else:
        print("no")
else:
    print('The while loop is over')
print('  Down')
