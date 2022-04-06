def average():

    while True:
        try:
            number_user = input("Please provide numbers with coma: ")
            split_numbers = number_user.split(".")
            num = [float(i) for i in split_numbers]
            mean = sum(num) / len(num)
            print(" Average ---> ",mean)
            break
        except(ValueError):
            print("Error occured")


if __name__ == "__main__":
    average()

