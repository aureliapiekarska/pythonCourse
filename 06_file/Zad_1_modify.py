import random

filename = input('Ask for directory?')

with open(filename) as fopen:
    quotes = fopen.readlines()

quote = random.choice(quotes).strip()
quote = quote.split(' - ')
width = len(quote[0]) * 2

print('Quote of the day: \n')
print(width * '*')
print(quote[0].center(width))
print(quote[1].center(width))
print(width * '*')