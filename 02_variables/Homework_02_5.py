#palindrom to wyrazenie...
quote = input('Podaj dowolne zdanie?')
print(quote)
quote2 = quote[::-1]

q1 = (quote.replace(' ', ''))
q2 = (quote2.replace(' ', ''))

print (q1 == q2)



