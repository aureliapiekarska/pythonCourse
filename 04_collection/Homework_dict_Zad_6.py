#Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
d1 = days.values()
print(d1)
d2 = set(d1)
print(d2)
d3=list(d2)
print(d3)
