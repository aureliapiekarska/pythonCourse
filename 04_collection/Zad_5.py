people = [
['Dorota', 'Wellman', 'dziennikarka'],
['Adam','Małysz','sportowiec'],
['Robert', 'Lewandowski', 'piłkarz'],
['Krystyna', 'Janda', 'aktorka']
]
for person in people:
    print('------------------')
    for elem in person:
        print(elem, end=' ')
    print()