age = int(input("Please enter you age: "))

if age >= 50:
    print("You're too old for this")
elif age >= 21:
    print("You're allowed!")
elif age >= 18:
    print("You're allowed with Parents!")
else:
    print("You're NOT allowed!")