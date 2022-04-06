import io

try:

    with open(filename,"r",encoding="utf-8") as f:
        f.readlines()

    with open("cos.txt","r",encoding="utf-8") as f:
        f.readlines()


    with open("error.txt","w",encoding="utf-8") as f:
        f.readlines()


    with open("error.txt","x",encoding="utf-8") as f:
        f.write("hello world")
except NameError:
    print("Błąd nazwy pliku")
except FileNotFoundError:
    print("Taki plik nie istnieje")
except io.UnsupportedOperation:
    print("NIe da rady")
except FileExistsError:
    print("Taki plik nie istnieje")

