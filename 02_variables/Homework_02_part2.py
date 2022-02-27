#Zadanie 4
book = input('Podaj tytul ksiazki?')
author = input('Podaj  nazwisko autora ?')
amount = input('Podaj liczbe stron?')

#sprawdz czy tytul i nazwisko...
print(book.isalpha())
print(author.isalpha())
print(amount.isnumeric())

#uzytkownicy bywaja leniwi...
print(book.title())
print(author.capitalize())

#polacz dane w jeden ciag...
book.split() #chcialam uzyc strip, ale wracalo ze spacja
print(book.replace(' ', ''))

#policz liczbe wszystkich znakow w napisie book
print(len(book))








