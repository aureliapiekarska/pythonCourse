def triangle_Pascal(n):

    for line in range(1, n + 1):
        total= 1;
        for i in range(1, line + 1):
            print(total, end=" ");
            total = int(total * (line - i) / i);
        print("");


if __name__ == '__main__':
    n = int(input("Podaj liczbę: "))
    triangle_Pascal(n)