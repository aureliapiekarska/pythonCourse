def game():

    word_guess = 'banannnnannnnnnnananaaana'

    duplicates = {}

    for n in word_guess:
        if n in duplicates:
            duplicates[n] += 1
        else:
            duplicates[n] = 1

    for key, value in duplicates.items():
        if value == n:
            print(key)
    print('n',duplicates[n])


game()