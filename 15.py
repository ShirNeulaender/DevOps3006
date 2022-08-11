# a = int(input("enter number: "))
# b = int(input("enter number: "))
# result = a / b
# print(result)

try:
    f = int(input("enter number: "))
    r = 5 / 0
except ZeroDivisionError:
    print("Couldn't divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("something went wrong, here is more")
    print(e.args)


# import requests

# try:
#    response = requests.get("htgf://github.com")
# except Exception as e:
#    print("something went wrong")
#   print(e.args)
