def min(a, b, c):
    if(a <= b) and (a <= c):
        smalest=a
    elif(b <= a) and (b <= c):
        smalest=b
    else:
        smalest=c

    return smalest

result = min(4,8,9)
print('Najmniejsza', result)