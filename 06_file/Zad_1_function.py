import random


# funkcja do pobrania tekstu, zwraca liste
def get_quotes():
    with open('quotes.txt') as fopen:
        quotes = fopen.readlines()

    return quotes


# funkcja wyświetlająca
def show(content):
    quote = random.choice(content).strip()
    quote = quote.split(' - ')
    width = len(quote[0]) * 2

    print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].center(width))
    print(width * '*')


# main code

quotes_list = get_quotes()
show(quotes_list)