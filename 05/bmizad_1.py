def bmi(weight, height):
    BMI_result = round(weight / (height ** 2), 2)

    if (BMI_result<18.5):
        return ("Masz niedowagę")
    elif BMI_result>25:
        return ("Masz nadwage")
    else:
        return ("Twoja waga jest prawidłowa")

result = bmi(56,1.6)
print('Twoje BMI', result)



