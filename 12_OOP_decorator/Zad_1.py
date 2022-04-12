def uppercase_decorator(fun):
    def up():
        txt = fun()
        txt = txt.upper()
        return txt

    return up

@uppercase_decorator
def some_function():
    txt = "dododo"
    return txt


print(some_function())