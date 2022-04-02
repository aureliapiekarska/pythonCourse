import random
with open('pass.txt', 'r') as fopen:
    lines = fopen.readlines()

word_guess = random.choice(lines).strip()
counter = len(word_guess)
gamer = input('Jak masz na imię drogi graczu? -> ')
print('Witam w grze wisielec', gamer)
print('Haslo sklada sie z ', counter, 'liter.')
turns = 6
print('Masz', 6, 'prob, aby odgadnac haslo')

def game(user_guess):
    turns=6
    user_guess = []
    used_letter = []
    for i in range(counter):
        user_guess.append('_')


    used_letters = ''

    while turns > 0:
        to_show = user_guess
        print(to_show)
        guess = input('Podaj litere,lub cale haslo jesli juz je znasz:')
        guess = guess.lower()

        if guess == word_guess:
            print('Wygrana! to jest to słowo:', guess)
            break

        if guess in word_guess:
            turns -=1
            for index in range(counter):
                if word_guess[index] == guess:
                    user_guess[index] = guess


        if not guess in word_guess:
            turns -= 1
            used_letter.append(guess)
            print('Uzyte litery',used_letter)

            for i in used_letter:
                if i in used_letter:
                    print('Nie mozesz uzyc tej litery ')
                else:
                    print('dupa')


        if turns == 0:
                print('Koniec gry')
                break

        print('Zostało Ci prób ->', turns)
        print('Podaj kolejna litere')

turns = 6
game(turns)