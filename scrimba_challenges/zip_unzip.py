nums = [1, 2, 3, 4]
# nums = "1234"
## each string item pairs with letter string -->
letters = ["a", "b", "c", "d"]
names = ["John", "Eric", "Michael", "Graham", "Joe"]

# create tuples within an array, key is nums and values are letters)
combo = dict(zip(nums, letters))
# making it a list is good for uneven element amount
combo_1 = list(zip(nums, letters, names))

# combo = list(zip(nums, letters))
print(combo)
print(combo_1)

# this will unzip it and turn it into tuples
num, let, nam = zip(*combo_1)
print(num, let, nam)

## unzip dictionaries
keys = "this parrot is deceased"
values = "denna papegojan är avliden"
### first split into lists
keys = keys.split()
values = values.split()
### this creates 2 lists 
print(keys, values)

en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)

# creating dictionary comprehension
new_dict = {key:value for key, value in zip(keys, values)}
print(new_dict)

# another way to create list of keys and values separately
en,sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en, sv)

# unzip
en1, sv1 = zip(*en_sv_dict.items())
print(en1, sv1)