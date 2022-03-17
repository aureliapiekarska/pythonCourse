str = input("Podaj ciag cyfr,liczb,znakow specjalnych ")
upper= 0
lower= 0
num = 0
special = 0
for i in str:
    if (i.islower()):
        lower = lower+1
    elif(i.isupper()):
        upper = upper+1
    elif(i.isdigit()):
        num = num+1
    elif not (i.isdigit()) and (i.islower()) and (i.isupper()):
        special = special+1


print('Lower case letters: ', lower)
print('Upper case letters: ', upper)
print('Number', num)
print('Special sign', special)