F_degree = 0
for number in range(0, 200):
        C_degree = round(5 / 9 * (F_degree - 32), 2)
        F_degree = F_degree + 20
        print(f'{F_degree} F is {C_degree} C')
