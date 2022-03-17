names_in_be = {'Belgium': ['Emma', 'Olivia', 'Louise', 'Mila', 'Elise', 'Alice', 'Lina', 'Juliette', 'Sofia', 'Camille']}
names_in_de = ['Mia', 'Emma', 'Hannah', 'Anna', 'Lea', 'Leonie', 'Lina', 'Marie', 'Sophia', 'Lena']
names_in_fr= ['Anna', 'Agathe', 'Agnes', 'Alice', 'Adrienne', 'Babette', 'Beatrice', 'Blanche', 'Brigitte', 'Camille']
names_in_pl =['Anna', 'Justyna', 'Ewa', 'Barbara', 'Kamila', 'Zofia', 'Julia', 'Elwira', 'Paulina', 'Patrycja']
names_in_uk =['Emma', 'Olivia', 'Louise', 'Mila', 'Elise', 'Alice', 'Lina', 'Juliette', 'Sofia', 'Camille']
names_in_se=['Mia', 'Emma', 'Hannah', 'Anna', 'Lea', 'Leonie', 'Lina', 'Marie', 'Sophia', 'Lena']
names_in_dk=['Anna', 'Agathe', 'Agnes', 'Alice', 'Adrienne', 'Babette', 'Beatrice', 'Blanche', 'Brigitte', 'Camille']
names_in_it = ['Anna', 'Justyna', 'Ewa', 'Barbara', 'Kamila', 'Zofia', 'Julia', 'Elwira', 'Paulina', 'Patrycja']
names_in_es = ['Emma', 'Olivia', 'Louise', 'Mila', 'Elise', 'Alice', 'Lina', 'Juliette', 'Sofia', 'Camille']
names_in_pt=['Mia', 'Emma', 'Hannah', 'Anna', 'Lea', 'Leonie', 'Lina', 'Marie', 'Sophia', 'Lena']

names_in_be['Germany'] = names_in_de
names_in_be['France'] = names_in_fr
names_in_be['Poland'] = names_in_pl
names_in_be['UK'] = names_in_uk
names_in_be['Sweden'] = names_in_se
names_in_be['Denmark'] = names_in_dk
names_in_be['Italy'] = names_in_it
names_in_be['Spain'] = names_in_es
names_in_be['Portugal'] = names_in_pt
print(names_in_be)

european_list = list(names_in_be.values())
print(european_list)

new_list = []
for lists in european_list:
    new_list += lists


for element in new_list:
    names_count = new_list.count(element)

print(set(new_list))


