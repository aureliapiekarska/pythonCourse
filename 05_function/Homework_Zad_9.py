def dict_creator(brand, year_1, oryginal):
    car_dict = {}
    car_dict['marka'] = brand

def old_car(year_1,oryginal):
    year = 2022
    if year - year_1 > 25 and oryginal > 75:
        print('Zabytek')
    elif year - year_1 > 25 and oryginal < 75:
        print('Jest za mlody')
    else:
        print('Samochod nie jest zabytkiem')

brand = (input("Podaj marke: "))
year_1= int(input("Podaj rocznik: "))
oryginal = int(input("Podaj % orginalnosci wdl. rzeczoznawcy: "))

dict_creator(brand,year_1,oryginal)
old_car(year_1,oryginal)