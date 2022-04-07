def number(i, j):

    if (i == 0):

        return j

    if (j == 0):

        return i

    if (i == j):
        return i

    if (i > j):
        return number(i - j, j)
    return number(i, j - i)

if __name__ == '__main__':
    i = int(input('Please provide first number: '))
    j = int(input('Please provide second number : '))
    print('GCD is equal to :', number(i,j))