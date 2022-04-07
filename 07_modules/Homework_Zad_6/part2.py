from check import generator as ig

def sequence(x):
    stri = x
    low = up = flow = fup = 0
    while up < len(stri):
        if stri[up] != stri[up - 1]:
            if fup - flow < up - low:
                flow, fup = low, up
            low = up
        up += 1
    if fup - flow < up - low:
        flow, fup = low, up
    return print('The longest repetition of the same character',stri[flow:fup])


def repeat():
    x = ig()
    print(x)
    sequence(x)

repeat()