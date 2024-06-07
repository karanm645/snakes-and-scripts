import random, string

friends_list = ["John", "Eric", "Michael", "Terry", "Graham"]

# for i in range(5):
# print(random.random()*6) # generates a number upto 6
# to specify ourselves we can use a different function called uniform
# print(random.uniform(1, 6)) # 5 numbers between 1 and 6
# print(random.randint(1, 6)) # this generates whole numbers (integers)
# print(random.randrange(2, 100, 2)) # 1st argument if 1 it will take odd numbers

# print(random.choice(friends_list))
# print(random.sample(friends_list, 2)) # no duplicates, use choices for duplicates
random.shuffle(friends_list)
print(friends_list)

smallcaps = "abcdefghijklmnopqrstuvwxyz"
largecaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

letters_numbers = string.ascii_letters + string.digits 

word = ''
for i in range(7): # for i in range 7 characters
  word += random.choice(letters_numbers) # this should generate a string of 7 characters

#if we dont want to repeat we could use
word_1 = "".join(random.sample(letters_numbers, 7)) # will never have duplicates

# instead of join we can use random choices
word = random.choices(letters_numbers, k=7)
print(word)

# for cryptogrophy use os or secrets modules