class Country():
    def __init__(self,name, area, language, population, capital):
        self.name = name
        self.area = area
        self.language = language
        self.population = population
        self.capital = capital

Spain = Country('Spain','505 944 km²', 'Spanish', '47,35 mil', 'Madrid')
France = Country('France', '643 801km²', 'French', '67 52 mil', 'Paris')
Poland = Country('Poland' ,'312 679 km²', 'Polish', '37,95 mil', 'Warsaw')


country_list = [Spain.__dict__, France.__dict__, Poland.__dict__]
print(country_list)
