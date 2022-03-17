#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są
#takie same.
items = ['koko', 'dido', 'koko']

counter = len(items)
first = items[0]
last = items[counter-1]
print(first == last)
print(items[0] == items[-1])
