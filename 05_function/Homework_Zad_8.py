def car_name():
    return str(input('Podaj markę auta: '))


def car_model():
    return str(input('Podaj model auta: '))


def car_old():
    return int(input('Podaj rocznik auta: '))


def check():
    auto = {'marka': car_name(), 'model': car_model(), 'rocznik': car_old()}
    print(auto)
    model = auto['model']
    zmienna = auto['rocznik']

    if 2022 - zmienna >= 25:
        return f'Gratulacje! Twój samochód {model} może być zarejestrowany jako zabytek.'
    else:
        return f'Twój samochód {model} jest jeszcze zbyt młody.'


print (check())