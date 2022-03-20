import random

def guess_game():
    number = random.randint (1, 10)
    guess_taken = 0
    guess = int(input('Podaj liczbe: '))
    guess_taken = guess_taken + 1
    if guess < number:
        if (number - guess) < 3:
                print ('Cieplo')
        else:
            print ('Zimno')
    elif guess > number:
        if (guess - number) < 3:
            print ('Cieplo')
        else:
            print ('Zimno')
    else:
        print('Udalo sie')

turns=8

while turns > 0:
    guess_game()
else:
    guess=turns
    print('Brawo')


