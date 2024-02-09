temperature = 13

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that returns the largest number among three numbers
x = 1
y = 2
z = 3
if x > y and x > z:
    print(x, "is the largest number")
elif y > x and y > z:
    print(y, "is the largest number")
else:
    print(z, "is the largest number")

# A program that checks a number is either even or odd
number = 56

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks a number is prime or not
b = 9

if b > 1:
    # Check for factors
    for i in range(2, b):
        if (b % i) == 0:
            print(b, "is not a prime number")
            print(i, "times", b//i, "is", b)

            break
    else:
        print(b, "is a prime number")