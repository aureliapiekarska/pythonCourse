# gra
import random
r_1 = int(input('podaj liczbe rund'))
opt = ['papier', 'kamien', 'nozyce']


score_p = 0
score_c = 0


while score_c or score_p <= r_1:
        figure = input('Papier, kamien, nozyce, podaj jedna figure:')
        com = (random.choice(opt))
        print(com)



        if (figure == 'papier') and (com == 'nozyce'):
                score_p += 1
                print('wygyrwa komp')
        elif (figure == 'nozyce') and (com == 'papier'):
                score_p +=1
                print('wygyrwasz')
        elif (figure == 'papier') and (com == 'kamien'):
                score_p+=1
                print('wygrywasz')
        elif (figure == 'kamien') and (com == 'papier'):
                score_c+=1
                print('wygrywa komp')
        elif (figure == 'kamien') and (com == 'nozyce'):
                score_p = score_p + 1
                print('wygrywasz')
        elif (figure == 'nozyce') and (com == 'kamien'):
                score_c+=1
                print('wygrywa komp')
        elif (figure == 'nozyce') and (com == 'nozyce'):
                score_c = score_p
                print('remis')
        elif (figure == 'papier') and (com == 'papier'):
                score_c = score_p
                print('remis')
        elif (figure == 'kamien') and (com == 'kamien'):
                score_c = score_p
                print('remis')


        if score_p == r_1:
                print("wygrałeś brawo "),
                break
        elif score_c == r_1:
                print("przegrales")
                break
        elif score_c + score_p == r_1:
                print("koniec"),
                break
        elif figure == 'ukraina':
                print(figure)
                break
print('koniec')


print('Masz:', {score_p}, 'Komputer:', {score_c})


