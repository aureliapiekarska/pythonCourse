#Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
x = int(input('Podaj liczbe'))
range_1 = (0, 9)
def inran(x):
    if x in range_1:
        print('Jest w zakresie')
    else:
        print('Nie jest w zakresie')

result =inran(x)


