class Wolf:
    paw = 4
    def __init__(self):
        print('I am wolf')
    def show_desc(self):
        print('Species of big animals,with great structure.')

class Dog(Wolf):
    def __init__(self, name, color, race, size):
        self.name = name
        self.color = color
        self.race = race
        self.size = size

nazar = Dog('Nazar', 'white', 'husky', 'big')

nazar.show_desc()



