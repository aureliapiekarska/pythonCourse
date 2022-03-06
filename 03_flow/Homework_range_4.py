# 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N....
num = int(input("Podaj liczbe nie wieksza niz 8: "))
factorial = 1
if num > 9:
   print(" Nie wykonam programu")
elif num == 0:
   print("0! to 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Silnia",num,"is",factorial)

