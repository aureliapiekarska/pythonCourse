#Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
e1=example_list.copy()
print('Kopia', e1)
s1=set(e1)
print('Ususniecie duplikatow',s1)
t1=tuple(s1)
print('Krotka', t1)
max_1 =max(t1)
print('Najwieksza',max_1)
min_1 =min(t1)
print('Najmniejsza',min_1)