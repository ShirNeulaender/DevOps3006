is_true = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
print(type(a == b))
if a < b and (b != 1 and strOne == "moshe" or strThree == "Three" or not strOne == "moshe"):
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("blabla")
else:
    print("something")

names = ["chanan", "tom", "zack", "aharon"]
other_list = ["aviel"]
name_to_find = "Ariel"
if name_to_find in names:
    print(name_to_find + " in list")

if len(other_list) > 0:
    print("other list has values")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if type(k) is int:
    print("I like numbers")
elif type(k) is str:
    print("I like strings!")
print(k == f)
print(k is f)
print(t == e)
print(t is e)




