# if you try to input string, error occurs
try:
    num = int(input("Enter a number between 1 and 30: "))
    # print("30 divided by", num, "is: ", 30/num) --> this moves to the else
    num1 = 30/num
    if num > 30:
      raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "You can't divide by zero!!")
except ValueError as err:
    # because we are expecting an integer
    print(err, num, "Bad Value, not between 1 and 30!")
except: 
    print("Invalid Input")
else:
    # if everything goes smoothly, so the first print statement
    print("30 divided by", num, "is: ", 30 / num)
finally:  
  print("**Thank you for playing**")


# --------------------------------------------#
# try:
# code you want to run
# except:
# executed if error occurs
# else:
# executed if no error
# finally:
# always executed
