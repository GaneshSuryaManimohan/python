""" Variable = A variable is a container for storing values. It can be a string, integer, float, boolean or any other data type. 
A Varible behaves as if it was the value it contains.
"""

# Variable declaration

# String variable
first_name = "John" 
food = "pizza"

print(first_name)

print("first_name") # this will print the string "first_name" instead of the variable value "John".

print(f"Hello, {first_name}") # Using f-string to print variable value.

print(f"Hello, {first_name}. Do you like {food}?") # f-string with mutliple variables.

# Integer variable
age = 30
quantity = 5

print(f"Hello, {first_name}. You are {age} years old")
print(f"You have {quantity} items in your cart")

# Float variable
price = 19.95
distance = 5.5
print(f"The price of the item is ${price}")
print(f"You walked {distance}kms today")

# Boolean Variable
is_student = False
for_sale = True
print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("The item is for sale")
else:
    print("The item is NOT available")