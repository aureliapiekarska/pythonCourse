class Animals():
    def animal(self):
        print('I am an animal')


class Mammals(Animals):
    def mammals(self):
        print('I am mamammal')

    def mamals_description(self):
        print('A mammal is an animal that has lungs, has heart')

class Cat(Mammals):
    def cat(self):
        print('Cat is species closely related to lion')


class Dog(Mammals):
    def dog(self):
        print('Dog is species closely related to wolf')



class Human(Mammals):
    def __init__(self):
        super(Human, self).mamals_description()
        print("I am human")


Dog().animal()
Cat().mammals()
Human()