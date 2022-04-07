def number(i):

    strong = 1

    if i <= 100000000:

        for i in range(2,i + 1):

            strong = strong * i

        print(strong)

    else:

        print('')

if __name__ == '__main__':

    i = int(input('Please provide the number : '))

    number(i)