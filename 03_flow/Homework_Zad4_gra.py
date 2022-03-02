# gra
import random
opt = ['papier', 'kamien', 'nozyce']
figure = input('Papier, kamien, nozyce, podaj jedna figure:')
com = (random.choice(opt))
print(com)

score_p = 0
score_c = 0

if (figure == 'papier') and (com == 'nozyce'):
    score_c = score_c + 1
    print('wygyrwa komp')
elif (figure == 'nozyce') and (com == 'papier'):
    score_p = score_p + 1
    print('wygyrwasz')
elif (figure == 'papier') and (com == 'kamien'):
    score_p = score_p + 1
    print('wygrywasz')
elif (figure == 'kamien') and (com == 'papier'):
    score_c = score_c + 1
    print('wygrywa komp')
elif (figure == 'kamien') and (com == 'nozyce'):
    score_p = score_p + 1
    print('wygrywasz')
elif (figure == 'nozyce') and (com == 'kamien'):
    score_c = score_c + 1
    print('wygrywa komp')
else:
    print('remis')

print('Masz:', score_p, 'Komputer:', score_c)
