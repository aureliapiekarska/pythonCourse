class Student(): #klasa
    def __init__(self,firstname,lastname,subject,university):
        self.firstname =firstname
        self.lastname = lastname
        self.subject = subject
        self.university = university
        self.email = f'{self.lastname}.{self.firstname}@{self.university}.pl'.lower()

obj_anna = Student('Anna','Kowalsks','informatyka','uam')


print(obj_anna.email)

obj_jan =Student('Jan','Kowalski','Biologia','PUT')

print(obj_jan.email)
