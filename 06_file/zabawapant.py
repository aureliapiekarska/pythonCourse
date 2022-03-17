sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
with open('pant.txt', 'w') as f:
    f.write('\n'.join(sweets_list))