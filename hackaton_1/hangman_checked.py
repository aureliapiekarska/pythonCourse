word_guess = 'slava'
used_letters = ''
gamer = input('Jak masz na imię drogi graczu?')
print('Witam w grze wisielec', gamer)
print('Haslo sklada sie z ', 5, 'liter.')
turns = 6
print('Masz', turns, 'prob, aby odgadnac haslo')

while turns > 0:
    count = 0
    for letter in word_guess:
        if letter in used_letters:
            print(letter)
        else:
            print('-')
            count += 1

    if count == 0:
        print('Brawo zgadles')
        break

    guess = input('Podaj litere,lub cale haslo jesli juz je znasz:')

    used_letters = used_letters + guess

    if not guess == used_letters:
        turns -= 1
        if turns == 0:
            print('Koniec gry')
            break
        if guess == word_guess:
            print('Wygrana! to jest to słowo:', guess)
            break

        print('Podaj kolejna litere')