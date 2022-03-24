def get_quotes():
    with open('quotes.txt') as fopen:
        quotes = fopen.readlines()
    print(quotes[0:5])
get_quotes()
