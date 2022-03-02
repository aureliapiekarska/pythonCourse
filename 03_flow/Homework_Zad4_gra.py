# gra
import random
opt = ['papier', 'kamien', 'nozyce']
figure = input('Papier, kamien, nozyce, podaj jedna figure:')
com = (random.choice(opt))
print(com)

if (figure == 'papier') and (com == 'nozyce'):
    print('wygyrwa komp')
if (figure == 'nozyce') and (com == 'papier'):
    print('wygyrwasz')
if (figure == 'papier') and (com == 'kamien'):
    print('wygrywasz')
if (figure == 'kamien') and (com == 'papier'):
    print('wygrywa komp')
if (figure == 'kamien') and (com == 'nozyce'):
    print('wygrywasz')
if (figure == 'nozyce') and (com == 'kamien'):
    print('wygrywa komp')
else:
    print('remis')
