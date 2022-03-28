def find():
    new_list = []
    x = int(input("Podaj kod do odszyfrowania: "))
    new_list.append(x)

    return new_list


def find2(new_list):
    for x in new_list:
        x = chr(x)
        print(x)




find2(find())
