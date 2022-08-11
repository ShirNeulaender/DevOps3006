# 1
# a = 1 / 0

# 1 + 2

try:
    a = 1 / 0
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Couldn't divide by zero")

# 3
try:
    x = 1
finally:
    print("finally")

# This code is legal , you can use finally instead except

# 4
# ValueError , ZeroDivisionError,BaseException,IndexError,SyntaxError,TypeError , etc...

# 5


# 6
# IOError- It is an error raised when an input/output operation fails
# ZeroDivisionError - division by zero

# 7
my_file = open("words.txt", "a")

# 8
my_file.write("Shir")

# 9
my_file = open("words.txt", "r")
file = my_file.read()
print(file)

# 10

my_other_file = open("something.txt", 'a', encoding="utf-8")
my_other_file.write("מה המצב?")
my_other_file = open("something.txt", 'r', encoding="utf-8")
other_file = my_other_file.read()
print(other_file)

# 11
from PIL import Image

img = Image.new('RGB', (60, 30), color='blue')
img.save('pillow_blue.png')
