# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych....
word = input('Podaj dowolny tekst?')

len_of_word = len(word)
for i in range(0, len_of_word, 2):
    print(i, word[i])
