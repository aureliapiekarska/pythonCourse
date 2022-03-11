import random

n = random.randint(1, 100)
win = n
guess = int(input('Wpisz liczbe 1 do 100'))

score_c = 0
score_p = 0

while n != guess:
    if guess < win:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 100: '))
        score_c = score_c + 1
    elif guess > win:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 100 '))
        score_c = score_c + 1
    elif guess == win - 10:
        print('Cieplo')
        score_c = score_c + 1
    elif guess == win + 10:
        print('Cieplo')
        score_c = score_c + 1
    elif win == guess:
        print('wygrales')
        score_p = score_p + 1
    if score_c == 5:
        break
print('Koniec gry nie masz wiecej szans')












