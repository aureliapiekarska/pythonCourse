txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.replace(',','')
txt = txt.lower()
words = txt.split()
print(words)

counting_dict = {}
for word in words:
    if word in counting_dict:
        counting_dict[word] += 1
    else:
        counting_dict[word] = 1
print(counting_dict)

for k, v in counting_dict.items():
    print(k, '----->', v)