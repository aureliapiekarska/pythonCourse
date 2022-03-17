book = {'Anna':'Poznan', 'Kasia':'Gdansk'}
book_translate = dict(book)
print(book)
q1 = input('Chcesz uktualnic slownik (tak/nie)?')
q2 = int(input('Ile razy chcesz wprowadzic zmiany'))
turns = q2

while turns > 0:
    count = 0
if q1 == 'nie':
    print('brak aktualizacji')

if q1 == 'tak':
    q_n=input('Podaj imie osoby:')
    q_c=input('Podaj miasto:')
    print(q_n)
    book_translate[q_n] = q_c
    print(book_translate)


    if q_n =='tak':
        turns -= 1
        print(q_n)
        if turns == 0:
            print('zakonczylem aktualizacje imion')
    if q_n == 'tak':
        turns -= 1
        print(q_c)
        if turns == 0:
            print('zakonczylem aktualizacje miast')

    book_translate[q_n] = q_c
    print(book_translate)

