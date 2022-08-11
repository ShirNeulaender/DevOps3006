# A
x = 4
y = 6

if x > y:
    print("BIG")
else:
    print("small")
# will print small

# B
for i in range(5):
    print(i)
# will print 0-4 numbers - the loop ran 5 times

# C
a = 3

if a > 3:
    print("spring")
elif a < 2:
    print("summer")
elif 1 < a < 3:
    print("winter")
else:
    print("fall")

# since a = 3 it will print "fall"

# D
count = 1
while count < 11:
    print(count)
    count = count + 1

# This loop will run 10 times , the last number that will be print is 10

# E
age = 27
f_name = "S"
shekel_dollar = 3.49
flew_abroad = True
apartment_number = 12

print(age)
print(shekel_dollar)
print(flew_abroad)
print(apartment_number)
print(f_name)

new = age + shekel_dollar
print(new)
# this will print all variables + print new variable with the result of 30.49

# F
phone_number = input("Please write your phone number: ")
print("phone number " + phone_number)


# Will get the phone number from the user and print it.

# G

def print_Hello(word="Hello"):
    print(word)
    return word


def calculate(number=5.2 + 3):
    print(number)
    return number


print_Hello()
calculate()


# print hello , 8.2

# H
def my_name(name=input("please write you name: ")):
    #  name = input("please write you name: ")
    print(name)
    return name


my_name()


# in row 82 it's not working for me, if im not pasting it in the method itself. why?


def my_number(number=input("wrote you phone number: ")):
    # number= input("wrote you phone number: ")
    number = int(number) / 2
    print(number)
    return number


my_number()


# also in wrote 94 same issue


# I
def summary(number1, number2):
    sum(number1, number2)
    return number1, number2


one = input("write a number: ")
two = input("write a number: ")
summary(one, two)


# This function isn't working for me , can you please guide me where did i wrong?

def string(str1=input("write a string: "), str2=input("write a string: ")):
    #   str1 = input("write a string: ")
    #  str2 = input("write a string: ")
    print(str1 + " " + str2)
    return str1, str2


string()

# K
for row in range(5):
    for col in range(row + 1):
        print("*", end='')
    print()

# L
for row in range(7):
    for column in range(7):
        if row == column or row + column == 6:
            print("*", end='')
        else:
            print(" ", end=" ")
    print()


# M
def numbers(number1=input("please enter a 3 digits number: ")):
    print(number1)
    return number1


numbers()


def new_numbers(number):
    y = number // 100
    y1 = (number - y * 100) // 10
    y2 = number - y * 100 - y1 * 10

    print(y)
    print(y1)
    print(y2)
    print("The sum is: ", y + y1 + y2)
