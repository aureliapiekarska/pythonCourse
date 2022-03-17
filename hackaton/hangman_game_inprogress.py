#wisielec
word_guess = 'slava'
letter_guess = ''
gamer = input('Jak masz na imię drogi graczu?')
print ('Witam w grze wisielec', gamer)
print('Haslo sklada sie z 5 liter.')
turns = 6
print('Masz', turns,'prob, aby odgadnac haslo')


while turns > 0:
    count = 0
    for letter in word_guess:
        if letter in letter_guess:
            print(letter)
        else:
            print('-')
            count += 1


    guess = input('Podaj litere,lub cale haslo jesli juz je znasz:')


    if not guess == letter_guess:
        turns -= 1
        print('Podaj kolejna litere')
        if turns == 0:
            print('Koniec gry')
        if guess == word_guess:
            break





