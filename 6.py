string_to_print = "Hello World!"
print(string_to_print * 5)

print(list(range(17, 2, -3)))

for i in range(7):
    print("hello world!")
    print(i)

names = ["chanan", "tom", "zack", "aharon"]

for name in names:
    if name == "zack":
        break
    #  break =python leave the loop
    else:
        pass
    print(name)

for i in range(len(names)):
    print(names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1

for name in names:
    if name == "aharon":
        continue
    # continue - stop the loop and start again
    print(name)


