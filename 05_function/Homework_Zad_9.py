def car_name():
    return str(input('Podaj markę auta: '))


def car_model():
    return str(input('Podaj model auta: '))


def car_old():
    return int(input('Podaj rocznik auta: '))


def car_oryginal():
    yes_not = str(input('Czy auto ma oryginalne części: '))
    if yes_not == 'tak':
        return True
    elif yes_not == 'nie':
        return False
    else:
        print('Podaj wartosć tak lub nie')
    return yes_not


def check():
    auto = {'marka': car_name(), 'model': car_model(), 'rocznik': car_old(), 'oryginalny': car_oryginal()}
    print(auto)
    model = auto['model']
    rocznik = auto['rocznik']
    oryginal = auto['oryginalny']

    if oryginal == True:
        if 2022 - rocznik >= 25:
            return f'Gratulacje! Twój samochód {model} może być zarejestrowany jako zabytek.'
        else:
            return f'Twój samochód {model} jest jeszcze zbyt młody.'
    else:
        return 'Auto nie moze byc zabytkiem'


print(check())