#Dictionaries
customer = {
    "name" : "John",
    "Age" : 30,
    "is_verified":True
}
print(customer["name"])# the spell should be same as mentioned in the Dictionarie or we can use get function
print(customer.get("BirthDate", "July 5, 1998"))# we can pass default values to avoid none return
customer["name"] = "Abhi"
print(customer["name"])
customer["DOB"] = "JULY 5, 1998"
print(customer["DOB"])
#Eg : convert entered numbers into words
phone_number = input("Phone number: ")
numbers_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
output = ""
for ch in phone_number:
    output += numbers_mapping.get(ch,"!") + " "
print(output)