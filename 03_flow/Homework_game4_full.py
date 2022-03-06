# papier kamien nozyce

import random
r_1 = int(input('podaj liczbe rund'))
koniec = True


def wydruk():
    print(f"Twój wybór: {wybor} przeciwko {kwybor} ale wojna ")


def checkpoint():
    print(f"Twoje punkty: {punkty1}, punkty komputera: {punkty2}")


while koniec:

    punkty1 = 0
    punkty2 = 0
    lista = ("papier", "kamień", "nożyce")

    while punkty1 or punkty2 <= r_1:
        wybor = input("\nwpisz swój wybór ")
        kwybor = random.choice(lista)
        wydruk()
        if wybor == kwybor:
            print("czyli remis, nikt nie otrzymuje punktu"), checkpoint()
        elif wybor == "nożyce" and kwybor == "papier":
            punkty1 += 1
            print("Nożyce tną papier, punkt dla Ciebie "), checkpoint()
        elif wybor == "nożyce" and kwybor == "kamień":
            punkty2 += 1
            print("Kamień stępił nożyce, niestety punkt dla mnie "), checkpoint()
        elif wybor == "papier" and kwybor == "kamień":
            punkty1 += 1
            print("Papier owija kamień, brawo "), checkpoint()
        elif wybor == "papier" and kwybor == "nożyce":
            punkty2 += 1
            print("Nożyce tną papier, punkt dla komputera"), checkpoint()
        elif wybor == "kamień" and kwybor == "papier":
            punkty2 += 1
            print("Papier owija kamień, twoja strata "), checkpoint()
        elif wybor == "kamień" and kwybor == "nożyce":
            punkty1 += 1
            print("Nożyce się stępiły "), checkpoint()

        if punkty2 == r_1:
            print("przegrałeś "), checkpoint()
            break
        elif punkty1 == r_1:
            print("wygrałeś brawo "), checkpoint()
            break

    koniec = input("czy chcesz grac dalej")
    if koniec == "ukraina":
        koniec = False