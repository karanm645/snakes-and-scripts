print("Guessing game")
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
num = 76
guess = 0
guess_limit = 5
guess_number = 0
guess = int(input(f"guess a number 1-100: "))
guess_number += 1
while guess_number < guess_limit:
    if guess != num:
        guess_number +=1
        if guess > num: 
            guess = int(input(f"{guess} Too high -- guess again 1-100: "))
        else: 
            guess = int(input(f"{guess} Too low -- guess again 1-100: "))
    if guess == num:
        print(f"You Win: you guessed the number {guess}")
        break
if guess != num:
    print(f'Sorry you lose! It was {num}')
        
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> guesses
# 2. What do I want to change each time?
#  -> guess number, number of guesses user takes
# 3. How long should we repeat?
#  -> until users loses runs out of guesses or wins

# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

# i = 0
# while i < 5:
#     i += 1
#     print(f"{i}." + "*" * i + "Loops are awesome" + "*" * i)
