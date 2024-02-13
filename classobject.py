# Class is a blueprint if an object
# An object is an instant of a class

class Person:
    # Properties/Attributes/Characteristics
    age = 53
    name = "Matthew"

    # Method/Function/Behaviour
    def talk(self):
        print("Person is talking")


teacher = Person()
print(teacher.name)
print(teacher.age)

