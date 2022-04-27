class animals():
    def animal(self):
        print('I am an animal')


class mammals(animals):
    def mammals(self):
        print('I am mamammal')

    def mamals_description(self):
        print('A mammal is an animal that has lungs, has heart')

class cat(mammals):
    def cat(self):
        print('Cat is species closely related to lion')


class dog(mammals):
    def dog(self):
        print('Dog is species closely related to wolf')



class human(mammals):
    def __init__(self):
        super(human, self).mamals_description()
        print("I am human")


dog = dog().animal()
cat = cat().mammals()
human = human()