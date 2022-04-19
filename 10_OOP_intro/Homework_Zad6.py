class employee():
    def __init__(self, position, salary, name, surname, work_experience):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.work_experience = work_experience


    def salary_inc(self):
        minimum_seniority = 1
        if self.work_experience >= minimum_seniority:
            salary_incbon = (self.salary * 0.03)+(self.salary * 0.11)
            print(salary_incbon)
            return salary_incbon
        if self.work_experience >= minimum_seniority * 2:
            salary_incbon = (self.salary * 0.05) + (self.salary * 0.11)
            print(salary_incbon)
            return salary_incbon

    def email(self):
        x = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = self.name + self.surname
        li = []
        for i in s:
            li.append(i)
        for i in li:
            if i in x:
                li.remove(i)
        y = ""
        for i in li:
            y += i
        return f"{y}@{self.company_name}.com".lower()


aurelia = employee("regulatory affairs",8000, "Aurelia", "Piek",5)
aurelia.salary_inc()
print(aurelia.email())