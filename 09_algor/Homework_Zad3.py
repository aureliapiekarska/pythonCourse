x = int(input('Please provide the number : '))
strong = 1

if x <= 100000000:
    for x in range(2,x + 1):
        strong = strong * x
    print(strong)
else:
    print('')