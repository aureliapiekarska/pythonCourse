import math

def deltain():
    a = int(input("Podaj a:"))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))

    delta = (b**2) - (4*a*c)
    print('\u0394')
    print(delta)
    print("Sinus argumentu delta --> ", math.sin(delta))


if __name__ == "__main__":
    deltain()