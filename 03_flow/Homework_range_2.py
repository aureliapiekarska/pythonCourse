#range, utworz liste na ulubione danie...
dish_list = ["chleb tostowy", "ser kozi", "ketchup"]
for index in range(3):
   print(index, ':', dish_list[index])
   if dish_list[index] == 'chleb tostowy':
       print(dish_list[index], 'wloz do opiekacza')
   if dish_list[index] == 'ser kozi':
       print(dish_list[index], 'wloz pomiedzy chleb tostowy i zamknij opiekacz')
   if dish_list[index] == 'ketchup':
       print('maczaj w', dish_list[index])







