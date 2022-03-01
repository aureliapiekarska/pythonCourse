F_degree = 0

while (F_degree <= 200):
    C_degree = round(5 / 9 * (F_degree - 32), 2)
    print(f'{F_degree} F is {C_degree} C')

    F_degree = F_degree + 20