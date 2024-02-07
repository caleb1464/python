# Data Types
number = 45  # int
num = 56.78  # float
greeting = "Hello there"  # str
IsPythonInteresting = True  # bool

# Variable storing multiple
languages = ["Pyhon", "PHP", "Java"]  # list
fruits = ("apple", "banana", "pineapple")  # tuple
countries = {"Kenya", "China", "USA"}  # set
# Dictionary
details = {"firstname": "Caleb",
           "age": 19,
           "course": "MIT",
           "nationalty": "Kenya"
           }

print(number)
print(greeting)
print(countries)
print(IsPythonInteresting)
print(details["course"])
print(details["nationalty"])

# Determining the data type
print(type(details))
print(type(countries))

# Type casting . converting one Data type to another
print(float(num))
print(int(number))
