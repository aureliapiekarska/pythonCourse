def number(i):

    empty_list = []

    j = 1

    while j < i:

        if j % 5 == 0:

            empty_list.append(j)

        elif j % 7 == 0:

            empty_list.append(j)
        j = j + 1

    print(empty_list)


if __name__ == '__main__':
    i = int(input('Please provide number: '))
    number(i)