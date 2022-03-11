books ={}
def ask_for_book():

    book_title =input('Podaj tytul ksiazki :')
    book_rate = input ('Podaj ocene od 1-10')
    books[book_title] = book_rate

for i in range(3):
    ask_for_book()
    print('----')
ask_for_book()

print(books)

