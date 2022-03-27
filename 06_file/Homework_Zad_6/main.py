def is_visa(card_number):
    return len(card_number) in [13, 16] and card_number[0] == '4'

def is_americanexpress(card_number):
    return len(card_number) == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')

def is_mastercard(card_number):
    start_with_1 = 51 <= int(card_number[0:2]) <= 55
    start_with_2 = 2221 <= int(card_number[0:4]) <= 2720
    return len(card_number) == 16 and (start_with_1 or start_with_2)

with open('card.txt', 'r') as fopen:
    lines = fopen.readlines()

def split_card(filename):
    with open(filename, 'w') as f:
        f.writelines(i)
    print(f'Karta {i} została dodana do {filename}.')
    return



for i in lines:
        i = i.strip('\n')
        if is_visa(i):
            split_card('visa.txt')
        elif is_mastercard(i):
            split_card('mastercard.txt')
        elif is_americanexpress(i):
            split_card('americanexpress.txt')
        else:
            print('To nie jest numer karty')
