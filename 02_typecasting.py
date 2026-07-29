# Typecasting is the process of converting a variable from one data type to another. str(), int(), float(), bool()

name = "Ethan"
age = 31
height = 5.9
quantity = 25
is_student = True

print(type(name)) # This will give type of "name" i.e string
print(type(age)) # This will give type of "age" i.e integer
print(type(height)) # This will give type of "height" i.e float
print(type(is_student)) # This will give type of "is_student" i.e Boolean

# Converting one data type to another
height = int(height)
print(height) # This will return the whole integer 5 instead of 5.9

age = float(age)
print(age) # This will return 31.0 

quantity = str(quantity)
print(quantity) # This will return 25, but the class will be string instead of integer
print(type(quantity))

# quantity += 5
# print(quantity) # You will get an error as an integer can't be added to a string

quantity += "7"
print(quantity) # This will return 257 which is joining of string

name = bool(name)
print(name) # This will return true. If we remove the name Ethan and keep it blank then it will return False.

