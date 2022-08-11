import ast
my_file = open("config.json")
configuration = dict(ast.literal_eval(my_file.read()))

try:
    env = dict(ast.literal_eval(my.file.read()))
except SyntaxError:
    print(f"unable to pharse(env_to_manage).json")
    exit(1)
