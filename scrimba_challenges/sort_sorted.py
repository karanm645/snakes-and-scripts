# sort vs sorting
# sort doesn't return anything, just sorts list
# sorted returns a new object that has been sorted
my_list = [1, 5, 3, 7, 2]
my_dict = {"car": 4, "dog": 2, "add": 3, "bee": 1}
my_tuple = ("d", "c", "e", "a", "b")
my_string = "python"

print(my_list, "original")
print(my_list.sort()) # wont work
print(sorted(my_list))
print(my_list, 'new')

print(my_tuple, "original")
# print(my_tuple.sort()) # wont work
print(sorted(my_tuple))
print(my_tuple, 'new')

print(my_dict, "original")
print(sorted(my_dict.items()), "key and values") # adds the values
print(sorted(my_dict.values()), "only values") # prints only the values
print(sorted(my_dict.values(), reverse=True), "reverse")  # reverse
print(my_dict, "new")

print(list(reversed(my_list)), "flips list around")
print(my_list[::-1], "flips it around again!")

my_list = [1, 5, -3, 7, -2]
my_llist = [["car", 4, 65], ["dog", 2, 30], ["add", 3, 10], ["bee", 1, 24]]
print(sorted(my_list, key=abs)) # you can use key to arrange list however you want
print(sorted(my_llist, key = lambda item :item[1]), "lambda") # lambda is a throw away, used for just one time in this case
