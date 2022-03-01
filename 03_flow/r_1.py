dish = "gzik"
if dish == "gzik":
    print('Wielkopolska')
else:
    print('Inny region')


text = 'kot'
for letter in text:
    print('- ')
for step in text:
    print("hello",step)

my_list = ["ada","julia","ruby"]
for step in my_list:
    print("hello", step)

for step in range(5):
    print("krok: ",step)

for l in range(5,10,2):
    print(l)

name_list = ["ada","julia","ruby"]
for index in range(3):
    print(index, ' : ', name_list[index])
word = 'abrakadabra'
len_of_word = len(word)
for i in range(0, len_of_word, 2):
    print(i, word[i])
