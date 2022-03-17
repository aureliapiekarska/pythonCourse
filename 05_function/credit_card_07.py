def is_visa(card_number):
    card_length = len(card_number)
    return  card_length in [13,16] and card_number[0]=='4'


def is_mastercard(card_number):
    card_length = len(card_number)
    starts_with_51_55=51<=int(card_number[0:2])<=55
    starts_with_2221_2720=2221 <=int(card_number[0:4])<=2720

    return card_length in [16] and ( starts_with_51_55 or starts_with_2221_2720)

def is_american_express(card_number):
    card_length = len(card_number)
    return card_length in [15] and (card_number[0:2] == '34' or card_number[0:2] == '37')



cards_lengths =[13,15,16]
card_number = input('podaj numer karty')

if not card_number.isdigit():
    print('To nie jest numer karty')
elif len(card_number) not in cards_lengths:
    print('Dlugos numeru karty nieprawidlowa')
else:
    if is_visa(card_number):
        print('To jest visa')
    elif is_mastercard(card_number):
        print('To jest master')
    elif is_american_express(card_number):
        print('To jest American')
    else:
        print('To jest inna karta')