dom = 1
szkola = 2
kosciol = 3
bar = 4
szpital = 5
kino = 6
teatr = 7

buildings = ['dom', 'szkola', 'kosciol', 'bar', 'szpital',
             'kino', 'teatr']

routes = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 4],
    4: [1, 3, 5],
    5: [2, 4, 6, 7],
    6: [3, 5, 7],
    7: [5, 6]
}

for start, neighbourhood in routes.items():
    for neighbour in neighbourhood:
        print(buildings[start - 1], '--->', buildings[neighbour - 1])
