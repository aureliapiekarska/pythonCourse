#zad 8 if

num_1 = input('Podaj liczbe 1:')
num_2 = input('Podaj liczbe 2:')
num_3 = input('Podaj liczbe 3:')


if (num_1 > num_2) and (num_1 > num_3):
    largest = num_1
    print('najwieksza 1')
elif (num_2 > num_3) and (num_2 > num_1):
    largest = num_2
    print('najwieksza 2')
else:
    largest = num_3
    print('najwieksza 3')

if (num_1 < num_2) and (num_1 < num_3):
    lowest = num_1
elif (num_2 < num_3) and (num_2 < num_1):
    lowest = num_2
else:
    lowest = num_3

if (num_2 > num_1 ) and (num_2 < num_3):
    middle = num_2
elif(num_3 > num_1) and (num_1 < num_2):
    middle = num_1
else:
    middle =num_3



print ('Kolejno', largest, middle, lowest)






