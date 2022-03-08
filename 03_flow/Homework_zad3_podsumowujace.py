str=input("Podaj ciag cyfr,liczb,znakow specjalnych ")
upper= 0
lower= 0
num = 0
special = 0
for i in range(len(str)):
    if(str[i]>='A' and str[i]<='Z'):
    upper += 1
    print("Upper case letters: ", upper)
    elif(str[i]>='a' and str[i]<='z'):
    lower += 1
    print("\nLower case letters: ", lower)
    elif(str[i]>='0' and str[i]<='9'):
    num+=1
    print("\nnumbers: ", num)
    else:
    special+=1
    print("\nSpecial characters: ", special)
