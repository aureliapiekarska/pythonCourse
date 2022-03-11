books = {
    'lotr': 3,
    'hp' : 10,
    'alicja':8
}

def show_book(title):
    print(f'Ksiazka {title}ma ocene--->{books[title]}')


print(books)

given_title =input('podaj tytul do spr')
show_book(given_title)