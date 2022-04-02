class Student(): #klasa
    university='UAM'
    def __init__(self,firstname,lastname,subject):
        self.firstname =firstname
        self.lastname = lastname
        self.subject = subject
        self.email = f'{self.lastname}.{self.firstname}@{self.university}.pl'.lower()

obj_anna = Student('Anna','Kowalsks','informatyka')


print(obj_anna.email)

obj_jan =Student('Jan','Kowalski','Biologia')

print(obj_jan.email)

