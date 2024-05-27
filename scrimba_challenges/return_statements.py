def value_added_tax(amount):
  tax = amount * 0.25
  total_amount = amount * 1.25
  # you can return in tuple, set or string!
  return f"{amount}, {tax}, {total_amount}"

price = value_added_tax(100) 
#if we dont have a return value, it returns empty object
print(price, type(price))