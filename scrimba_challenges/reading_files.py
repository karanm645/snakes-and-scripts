# using context manager
with open("scrimba_challenges/friends.csv", 'r') as f:
  #print(f.read(50))
  friends = f.read().splitlines()
  #print(friends)
  for friend in friends:
    friend = friend.split(',')
    name = friend[0]
    year = int(friend[1].strip(""))
    print(f"In 2030, {name} will be {2030 - year} years old")
    

with open("scrimba_challenges/movies.txt", "r") as f: 
  for line in f:
    print(line)

# long way ##########
# my_file = open("scrimba_challenges/greeting.txt", "r")  # w is used for overriding the file and a for appending
# #print(my_file.read())

# # if files are too long, we can have a certain amount of characters render
# print(my_file.read(10))

# # we can read line by line
# print(my_file.readline())
# # read next line
# print(my_file.readline())

# # read and structure (break up) line by line
# line_by_line = my_file.readlines()
# line_by_line_1 = my_file.read().splitlines()
# print('readlines: ', line_by_line)
# my_file.close()