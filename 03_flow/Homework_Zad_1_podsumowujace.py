names = input('Podaj imiona tak, aby przed nowym i po kazdym imieniu byla spacja?')
names.split(' ')
for index in names:
    if index == ' ':
        print(names.replace(' ', ' Witaj '))
        continue
        print(names.replace(' ', 'Witaj '))
    if index == '':
        break
        print(koniec)



