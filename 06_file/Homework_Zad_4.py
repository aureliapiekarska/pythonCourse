import random


# funkcja do pobrania tekstu, zwraca liste
def get_quotes():
    with open('quotes.txt') as fopen:
        quotes = fopen.readlines()
    return quotes


# funkcja wyświetlająca
def show(content):
    quote_1= random.choice(content).strip()
    quote_2 = random.choice(content).strip()
    quote_3 = random.choice(content).strip()


    print('Quote of the day: \n')

    print(quote_1)
    print(quote_2)
    print(quote_3)



# main code
quotes_list = get_quotes()
show(quotes_list)