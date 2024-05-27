def greeting(name,age=28):

  print("hello " + name + " my friend who is " + str(age))
  # you have to specify f for format before string to concactenate 
  print(f"Hello {name}, you are {age}")
name = input("enter your name: ")
greeting(name, "22")
greeting(name)
