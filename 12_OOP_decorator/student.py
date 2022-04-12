class Student:
  university = 'university'
  promotion = 3.0

  def __init__(self, name, last, grades):
    self.name = name
    self.last = last
    self.grades = grades

  def __repr__(self):
    return self.name.capitalize() + " " + self.last.capitalize()

  def email(self):
    return f'{self.last}.{self.name}@university.com'

  def promotion_to_next_year(self):
      if self.grades > self.promotion:
          print("You go to next year")
      else:
          print("You need to make the same year again")

  @classmethod
  def set_new_promotion(cls, new_value):
      cls.promotion = new_value

obj_anna = Student('Aurelia', 'kowalska', 2.8)
obj_michal = Student('Wiktor', 'nowak', 4.0)
obj_michal.set_new_promotion(2.5)

print(obj_anna.promotion)
print(obj_michal.promotion)
print('****')
Student.set_new_promotion(4.1)
print(obj_anna.promotion)
print(obj_michal.promotion)