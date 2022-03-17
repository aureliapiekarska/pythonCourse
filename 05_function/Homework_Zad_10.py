#wisilece z hackatonu
word_guess = 'slava'
counter = len(word_guess)

user_guess = []
for i in range(counter):
    user_guess.append('_')

print(user_guess)

used_letters = ''
gamer = input('Jak masz na imię drogi graczu? -> ')
print('Witam w grze wisielec', gamer)
print('Haslo sklada sie z ', counter, 'liter.')
turns = 6
print('Masz', turns, 'prob, aby odgadnac haslo')

while turns > 0:
    to_show = '_'.join(user_guess)
    print(to_show)
    guess = input('Podaj litere,lub cale haslo jesli juz je znasz:')
    guess = guess.lower()

    if guess == word_guess:
        print('Wygrana! to jest to słowo:', guess)
        break

    if guess in word_guess:
        for index in range(counter):
            if word_guess[index] == guess:
                user_guess[index] = guess

    else:
        print('Nie ma tej litery w słowie')
        turns -= 1
        if turns == 0:
            print('Koniec gry')
            break

        print('Zostało Ci prób ->', turns)
        print('Podaj kolejna litere')