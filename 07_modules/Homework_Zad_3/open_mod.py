def openfile():
    filename = input('Podaj nazwe pliku')
    with open(filename) as fopen:
        quotes = fopen.readlines()

    print(quotes)

openfile()