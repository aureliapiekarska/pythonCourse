def is_american_express(card_number):
    card_length = len(card_number)
    return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')


def is_visa(card_number):
    card_length = len(card_number)
    return card_length in [13, 16] and card_number[0] == '4'


def is_mastercard(card_number):
    card_length = len(card_number)
    starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
    starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720

    return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)

def get_card_number():
    cards_lengths = [13, 15, 16]
    while(True):
        card_number = input('Podaj numer karty: ')
        card_number = card_number.replace(' ', '')

        if card_number.isdigit() and len(card_number) in cards_lengths:
            break
        else:
            print('To nie jest nr karty, spróbuj jeszcze raz ')

    return card_number


#--- main code

card_number = get_card_number()
print('Numer karty użytkownika -->', card_number)

if is_visa(card_number):
    print("To jest visa")
elif is_mastercard(card_number):
    print("To jest master card")
elif is_american_express(card_number):
    print("To jest american express")
else:
    print("To może być inna karta")