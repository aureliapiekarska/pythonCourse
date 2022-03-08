print('Podaj wymiar tablicy.')
n = int(input())

array = [['_'] * n] * n
print(array)
print('--------------')

for row in array:
    for col in row:
      print(col, end=' ')
    print()