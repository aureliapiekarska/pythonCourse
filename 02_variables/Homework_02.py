
# zmodyfikuj skrypt tak, aby przyjmowal wartosci od uzytkownika
distance = input('Podaj dlugosc trasy [km]')
distance = int(distance)
cost = input('Podaj koszt benzyny [PLN]')
cost = int(cost)
usag = input('Podaj spalanie na 100 [l]')
usage = int(usag/100)
result = (distance * cost * usage)
print('Koszt wyprawy bedzie wynosi=', result)