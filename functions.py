# Inbuilt functions
number = max(89, 70, 23, 45, 123)
print(number)

x = min(78, 45, 88, 76)
print(x)

v = pow(2, 3)
print(v)


# User-defined functions
def src():
    print("Caleb")


# Calling a new function
src()


def student():
    name = "Caleb"
    age = "19"
    course = "MIT"
    print(name, age, course)


student()


# Parameters/variables and arguments/values

def students(name, age, course):
    print(name, age, course)


students("Caleb", 19, "MIT")
students("Nancy", 18, "MIT")
students("Matthew", 19, "MIT")
students("Agnes", 16, "MIT")
students("Mark", 19, "MIT")


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Caleb", 19, "Male", "CEO", "Ksh. 50000")
employees("Mary", 23, "Female", "Managing Director", "Ksh. 42000")
employees("Sylvia", 20, "Female", "Secretary", "Ksh. 35000")
employees("John", 35, "Male", "Driver", "Ksh. 15000")
employees("Benson", 18, "Male", "Janitor", "Ksh. 8900")
