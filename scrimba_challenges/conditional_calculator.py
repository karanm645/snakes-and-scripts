print("if elif else - Exercise")
# Create a calculator which handles +,-,*,/ and
# # outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode
# # so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

mode = input('enter math operation(+,-,/,*), or f for celcius to farenheit conversion: ')
num1 = float(input('input first number: '))
if mode.lower() == "f":
  print(f'{num1} celcius is equivalent to {(num1 * 9/5) + 32} farenheit')
else:
  num2 = float(input('input second number: '))

  if mode == '+':
    print(f'answer is {num1 + num2}')
  elif mode == '-':
    print(f'answer is {num1 - num2}')
  elif mode == '*':
    print(f'answer is {num1 * num2}')
  elif mode == '/':
    print(f'answer is {num1 / num2}')
  else:
    print('input error')


# num_1 = input("First Number: ")

# num_2 = input("Second Number: ")
# calc = input("-, +, /, or * ? ")
# def calculate(num_1, num_2):
#     if calc == "-":
#         int(num_1) - int(num_2)
#     elif calc("add"):
#         int(num_1) + int(num_2)
#     elif calc("multiply"):
#         int(num_1) * int(num_2)
#     elif calc("divide"):
#         int(num_1) / int(num_2)
# print(calculate(num_1, num_2))