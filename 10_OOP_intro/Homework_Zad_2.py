class orchid():
    def __init__(self,blooming,species,color):
        self.blooming = blooming
        self.species = species
        self.color = color

    def water(self):
        return 'pur pur water is coming'

    def sun(self):
        return 'put on sun'


Pink = orchid('morning','pink lady species','pink')
Bee = orchid('night','bee orchid','purple')
Disa = orchid('midnight','disa uniflora','red')
print(Pink.__dict__)
print(Pink.water())
print(Pink.sun())

print(Bee.__dict__)

print(Disa.__dict__)
