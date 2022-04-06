class mammals():
    def __init__(self,hair,warm_blooded,four_chambered_heart,species):
        self.hair= hair
        self.warm_blooded = warm_blooded
        self.four_chambered_heart = four_chambered_heart
        self.species = species

    def procreation(self):
        return 'make more of us, one mammal, two mammals ...... extend our line'


Dog = mammals('yes','yes','yes','dog')
Sfinks= mammals('no','yes','yes','cat:sfinks')

print(Dog.__dict__)
print(Dog.procreation())


print(Sfinks.__dict__)

