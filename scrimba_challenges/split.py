msg = "Welcome  to  Python  101: Split  and Join"
csv = "Eric,John,Michael,Terry,Graham"
friends_list = ["Eric", "John", "Michael", "Terry", "Graham"]

#create array for csf string with each object splitted after comma
print(csv.split(","))

#join friends list to a string --> get out of array
print(' - '.join(friends_list))

#join two lists
print(' - '.join(friends_list + friends_list))

# join is string, split is array
# if we want to strip out all of spaces from string

#split the msg into a list and join
print(''.join(msg.split()))

#using replace
print(msg.replace(" ", " == "))
