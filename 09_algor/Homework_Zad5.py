def split_sort(names):

    words = names.split()
    words.sort()
    for i in words:
        print(i)


if __name__ == '__main__':
    names ='Piekarska Lipski Kowal Adamiak Wojtczak Nowak Kowalski'
    split_sort(names)