books ={}
def save_book():

    book_title =input('Podaj tytul ksiazki :')
    book_rate = input ('Podaj ocene od 1-10')
    books[book_title] = book_rate

def show_book(title):
    print(f'Ksiazka {title}ma ocene--->{books[title]}')

for i in range(3):
   save_book()
   print('----')

print(books)

while(True):
    given_title = input('Podaj tytul do oceny')
    if given_title in books.keys():
        break
    print('nie ma takiego tytulu')
show_book(given_title)
