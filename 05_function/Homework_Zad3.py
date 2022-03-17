#maximus_of(a,b,c)

def max(a, b, c):
    if(a >= b) and (a > c):
        largest=a
    elif(b >= a) and (b >= c):
        largest=b
    else:
        largest=c

    return largest
result = max(4,11,12)
print('Najwieksza',result)

