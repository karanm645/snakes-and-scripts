name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross: ").lower()
  
    if answer == "swim":
        print("you swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles and ran out of water - you lose!")
    else:
        print("not a valid option. you lose")
  
elif answer == "right": 
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("Back to main road, you lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, do you talk to them? (yes/no)")
        
        if answer == "yes":
          print("you talk to the stranger and won the game and get gold!")
        elif answer == "no":
          print("Stranger offended, you lose")
        else:
          print("not a valid option, you lose")
    else:
        print("not a valid option. you lose")
else:
    print("Not a valid option. You lose.")
print("Thank you for trying", name)