# bmi
weight = int(input('Podaj wage(kg):'))
height = int(input('Podaj wzrost (cm):'))
p = range(18,25)
BMI = (weight / height**2) * 10000
print("Moje BMI", BMI)
if BMI == p:
    print('waga normalna')
elif BMI > 25:
    print('nadwaga')
elif BMI < 18:
    print("niedowaga")

