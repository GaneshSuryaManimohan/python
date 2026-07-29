# input() = A function that prompts the user to enter data.
#           Returns the entered data as a string

uname = input("Please enter username: ")
yob = input("Enter your Year of birth: ")
age = input("Enter you age: ")

age = int(age) + 1 # We need to convert age to integer as the input will by default consider it as a string

# The other way to do this is by typecasting the input of age with int:
# Ex: age = int(input("Enter your age: "))
#     age = age + 5


# print(f"Your username is {uname}, born in {yob}")

print(f"Username {uname}")
print("Welcome to Python Learning")
print(f"Your year of birth is: {yob}")
print(f"You are {age} years old")