import random

def main():
    x = range(10)
    y = random.choices(x,k= 10)
    additional_number = random.choice(y)
    additional_number_int = int(additional_number)
    y.append(additional_number_int)
    print(y)


def generator():
    x = input('Please provide 4 signs')
    y = random.choices(x,k= 10)
    y2 = ""
    for i in y:
        y2 += i
    return y2



if __name__ == "__main__":
    main()
