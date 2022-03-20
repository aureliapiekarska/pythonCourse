def data_car(brand,model,year_1):
    car_dict = {}
    car_dict["marka"] = brand
    car_dict["model"] = model
    car_dict["rocznik"] = year_1
    print(car_dict)

def check(model,yeer):
    year = 2022
    if year - year_1 >= 40:
        print(f"Samochod {model}jest zabytkiem")
    else:
        print(f"Twój samochód {model} nie jest zabytkiem")

brand = str(input("Podaj marke: "))
model = str(input("Podaj model: "))
year_1 = int(input("Podaj rocznik: "))

data_car(brand,model ,year_1)

check(model,year_1)