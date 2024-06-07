# def func(n):
#   return lambda a: a*n

# print(type(func(3))) # return value is a function, so function is taking a function that is inputting the n value
# # lets create a new function
# doubler = func(2)
# print(doubler(10))

# quintipler = func(5)
# print(quintipler(10))

# consultancy example
def price_calc(start, hourly):
  return lambda hours: start + hourly * hours

# we have created functions that we can re-use like below
walk_in_cost = price_calc(10, 30)
premium_cost = price_calc(1, 25)
print(walk_in_cost(2))
print(premium_cost(2))

print(price_calc(1, 25)(2))
print((lambda a,b,c: a+b+c)(2,3,4)) #positional arguments
print((lambda a,b,c: a+b+c)(b=3,c=3,a=10)) #name your arguments
print((lambda *args: sum(args))(2, 3, 4, 50)) # you can use this to add more arguments
