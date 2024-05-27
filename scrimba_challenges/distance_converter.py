name=input("What is your name?: ")
kilometers=float(input(f"Hi {name} How many kilometers would you like to convert?: "))
conversion= 0.621371
miles = float(kilometers * conversion)
print(f"Hi {name.title()}!, you entered {kilometers} km's which is {round(miles, 1)} miles")
