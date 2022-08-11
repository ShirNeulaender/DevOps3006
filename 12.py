my_file = open("Read.txt")
# print(list(my_file.readlines()))
my_file.seek(1)
for line in my_file.readlines():
    print(line)
