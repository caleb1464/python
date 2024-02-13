class Person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")


teacher = Person("Joel", 23, "Male")
accountant = Person("Agnes", 31, "Female")
doctor = Person("Timothy", 49, "Male")
print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.firstname, accountant.age, accountant.gender)
