# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 u...
n = 6
guess = int(input('Wpisz liczbe 1 do 20 '))
while n != "guess":
    print
    if guess < n:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 20: '))
    elif guess > n:
        print('Zimno')
        guess = int(input('Wpisz ponownie liczbe od 1 do 20: '))
    else:
        print('zgadles')
        break
    print
