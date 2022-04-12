#functions with Parameters and Keyword Arguments
def greet_user(first_name,last_name):#always define functions 1st and call them later
    print(f'hi there {first_name} {last_name}')
    print("welocom aboard ")
print("Start")
greet_user("John", "Smith")
greet_user("Smith", "John")
greet_user(last_name="Smith", first_name="John")#keyword arguments we can only assign to 2nd parameters
print("finish")