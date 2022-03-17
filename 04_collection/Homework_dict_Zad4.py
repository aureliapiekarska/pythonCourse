#4 Mnozenie
rows=10
columns=10
for i in range(1,rows+1):
    for k in range(1,columns+1):
        array = i*k
        print("{:2d} ".format(array),end='')
    print("\n")