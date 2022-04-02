import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('----Twoja porada:')
    print(content)

def get_user_data():
    while True:
        try:
            weight = float(input('Podaj swoją wagę [kg]: '))
            height = float(input('Podaj swoj wzrost [m]: '))

            if weight > 597 or height > 2.8:
                raise ValueError('Nieprawdopodobne wartości')
            break
        except:
            print('Wartość nieprawidłowa, spróbuj jeszcze raz')
    return weight, height

def main():
    w, h = get_user_data()
    result = bmi.get_bmi_value(w, h)
    show_advice(result)


if __name__ == '__main__':
    main()