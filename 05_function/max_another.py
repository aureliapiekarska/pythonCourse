def max_of(x, y):
    if x > y:
        return x
    else:
        return y

def maximum_of(a,b,c):
    result = max_of(a, b)
    max_value = max_of(result, c)
    return max_value


# --- main
print("Największa wartość to",  maximum_of(4, 91, 28) )