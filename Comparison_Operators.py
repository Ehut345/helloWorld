#Comparison Operators( >, <, >=, <=, ==, !=)
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
#eg
name = input("Enter your name: ")
if len(name) < 3:
    print("Name should be more than 3 Characters")
elif len(name) > 50:
    print("Name shouldn't be more than 50 Characters")
else:
    print("Name looks good!")
#Eg 1 Weight Converter Program
weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your are {converted} in Kgs")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"Your are {converted} in Lbs")