# all purchases under 50 dont need a pin code to be approved
amount = 70
if amount <= 50:
  print("Purchase approved")
else:
  print("Please enter your pin")

is_raining = False
is_cold = True 
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and Jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")
