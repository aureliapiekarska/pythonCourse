import random

num = random.randint(1, 20)
count = 0


def take_input():
    guess = int(input('Podaj liczbe'))
    if (guess >= 0 and guess <= 20):
        return guess
    else:
        print("Nie udalo sie")
        return guess
        take_input()


guess = take_input()

while (num != guess):
    if (num < (guess + 5) and num > (guess - 5)):
        print('cieplo')
        guess = take_input()
        count = count + 1
    else:
        print('zimno')
        ans = take_input()
        count = count + 1

if count == 0:
    print('Zgadles')
