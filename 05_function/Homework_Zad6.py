# gra
import random
r_1 = int(input('podaj liczbe rund'))
opt = ['papier', 'kamien', 'nozyce']
score_p = 0
score_c = 0

def gameresults(score_p,score_c):
        if score_p == r_1:
                print("wygrałeś brawo ")
        elif score_c == r_1:
                print("przegrales")
        elif score_c + score_p == r_1:
                print("koniec"),

def game(r_1):
        score_p = 0
        score_c = 0
        while score_c or score_p <= r_1:

                opt = ['papier', 'kamien', 'nozyce']
                figure = input('Papier, kamien, nozyce, podaj jedna figure:')
                com = (random.choice(opt))
                print(com)


                if (figure == 'papier') and (com == 'nozyce'):
                        score_c += 1
                        print('wygyrwa komp',score_c)
                elif (figure == 'nozyce') and (com == 'papier'):
                        score_p +=1
                        print('wygyrwasz',score_p)
                elif (figure == 'papier') and (com == 'kamien'):
                        score_p+=1
                        print('wygrywasz',score_p)
                elif (figure == 'kamien') and (com == 'papier'):
                        score_c+=1
                        print('wygrywa komp',score_c)
                elif (figure == 'kamien') and (com == 'nozyce'):
                        score_p += 1
                        print('wygrywasz',score_p)
                elif (figure == 'nozyce') and (com == 'kamien'):
                        score_c+=1
                        print('wygrywa komp',score_c)
                elif (figure == 'nozyce') and (com == 'nozyce'):
                        score_c = score_p
                        print('remis',0)
                elif (figure == 'papier') and (com == 'papier'):
                        score_c = score_p
                        print('remis',0)
                elif (figure == 'kamien') and (com == 'kamien'):
                        score_c = score_p
                        print('remis',0)
                if score_p+score_c==r_1 or score_p==r_1 or score_c==r_1:
                        break

a = score_p
b = score_c
gameresults(a,b)

game(r_1)


