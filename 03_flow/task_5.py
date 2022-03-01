password = input("Podaj haslo")

if len(password) < 8:
    print ("haslo musi miec przynajmnie 8 znakow")
elif password.islower():
    print("haslo musi miec pduza litere")
elif password.isupper():
    print("haslo musi miec mala litere")
elif password.isalpha() or password.isdigit():
    print ("haslo musi miec zarowno cyfyr i litere")

else:
    print("poprawne haslo")