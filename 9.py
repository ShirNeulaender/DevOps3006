def print_hello(name):
    if name != "michael":
        print(f"hello {name}")


print_hello("shir")


def greet_name(name, excluded_name, greeting_word):
    if name != excluded_name:
        return f"{greeting_word} {name}"


def multiply(x, y):
    from utils import important_var
    result1 = x * y
    result2 = x / y
    print(result1, result2)
    return result1, result2


user_name = input("enter your name: \n")
print(greet_name(user_name, "aviel", "hello"))
multiply(10, 4)

