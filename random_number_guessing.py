import random
guess = random.randint(1,10)
tries = 3
while tries > 0:
    number = int(input('guess the number: '))
    if number == guess:
        print('you guessed correctly')
        tries = 0
    elif number != guess:
        if guess > number:
            print('it\'s bigger')
            tries = tries - 1
        else:
            print('it\'s smaller')
            tries = tries - 1
