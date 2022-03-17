import random
filename ='/Users/aurelia/Desktop/quotes.txt'
with open(filename, 'r') as fopen:
    quotes = fopen.readlines()

quote = random.choice(quotes).strip()
width = len(quote * 2)

print('Quote of the day \n')
print(width * '*')
print(quote.center(width))
print(width * '*')