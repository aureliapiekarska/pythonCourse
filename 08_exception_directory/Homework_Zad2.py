tup = (13,'dodo',{'aksolot',5},[1,1,1,1,1,1,1,])

def replacement():
    try:
        index = int(input("Provide index: "))

        print(tup[index])

        x = tup[index] = input("What you want to replace ")

    except TypeError:

        print("Error")


if __name__ == "__main__":
    replacement()