import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('----Twoja porada:')
    print(content)


def main():
    w = float(input('Podaj swoją wagę [kg]: '))
    h = float(input('Podaj swoj wzrost [m]: '))
    resutl = bmi.get_bmi_value(w, h)
    show_advice(resutl)


if __name__ == '__main__':
    main()