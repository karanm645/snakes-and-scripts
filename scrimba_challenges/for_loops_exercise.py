names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]
msg = "You are invited to the party on Saturday"

# combine two lists
names.extend(names1)

# input
for index in range(2):  
  names.append(input("Enter a new name: "))
  
# print out invitations
for name in names:
  msg1 = f"{name.title()}! {msg}"
  print(msg1)
  
  
  
  
  
# # print out invitation for each friend using for loops
# for name in names:
#   print(f"{name.capitalize()}! You are invited to the party on Saturday.")
# # add two extra names to the list using an input box

# # print one invitation per each friend per line

# # Name should be capitalized
