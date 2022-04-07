class Dog():
    def __init__(self,name,color,race):
        self.name = name
        self.color = color
        self.bread = race

    def bark(self):
        return'hau'*100

    def wave_tail(self):
        return 'machu machu'


Lord = Dog('Lord', 'black', 'spaniel')
Nazar = Dog('Nazar','white','husky')
Baron = Dog('Baron','brown','retriver')
print(Lord.__dict__)
print(Lord.bark())
print(Lord.wave_tail())

print(Nazar.__dict__)
print(Nazar.bark())
print(Nazar.wave_tail())

print(Baron.__dict__)
print(Baron.bark())
print(Baron.wave_tail())