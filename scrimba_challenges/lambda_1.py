# def square(x):
#   return x*x 
# # structure: name = lambda parameter(s): expression
# double_multiplication = lambda x,y: 2*x*y #return value always implicit

# # we could do a single line function definition
# def square2(x): return x*x
# # print(double_multiplication(2, 4))

# def name_and_alias(name, alias):
#   return name.strip().title() + ":" + alias.strip().title()

# name_and_alias_1 = lambda name,alias: name.strip().title() + ": " + alias.strip().title()


# def name_and_alias_3(name, alias): return name.strip().title() + ": " + alias.strip().title()
# print(name_and_alias_3(" SHanue Lopze ", "Shay Shay "))

monty_python = [
    "John Marwood Cleese",
    "Eric Idle",
    "Michael Edward Palin",
    "Terrence Vance Gilliam",
    "Terry Graham Perry Jones",
    "Graham Arthur Chapman",
]
# regular function example
def sort_names(name):
  return name.split(" ")

# lambda created
monty_python.sort(key = lambda name: name.split(" ")[-1]) #order by last name use [-1]
print(monty_python)

# use of function created above
monty_python.sort(key = sort_names)
print(monty_python)
