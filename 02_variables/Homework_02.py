
# zmodyfikuj skrypt tak, aby przyjmowal wartosci od uzytkownika
distance = input('Podaj dlugosc trasy [km]')
distance = float(distance)
cost = input('Podaj koszt benzyny [PLN]')
cost = float(cost)
us = input('Podaj spalanie na 100 [l]')
us = float(us)
usage = (us/100)
result = (distance * cost * usage)
print('Koszt wyprawy bedzie wynosil=', result)

#Czy 43 - 13 będzie się równać 11 + 12 ?
a = 43  - 13
b = 11 + 12
print (a == b)

#Czy dzielenie 129 przez 17 bez reszty wynosi 3?
c = 129 // 17
print (c == 3)


#Czy 247 podzielone przez 5 daje resztę 2?
d = 247 % 5
print (d == 2)

#stworz dwie zmienne s1 i s2 przechowujace dowolne wyrazy...
s1 = 'butter'
s2 = 'fly'
center_s1= len(s1) // 2
s11 = (s1[0:2])
s111 = (s1[3:5])
print(s11 + s2 + s111)




