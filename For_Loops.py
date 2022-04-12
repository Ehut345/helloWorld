#For Loops
for item in 'Python':
    print(item)
for item in ['john','mosh','sarah']:
    print(item)
for item in [1,2,3,4]:
    print(item)
for item in range(10):#range(max range)
    print(item)
for item in range(5,10):#range(min range, max range)
    print(item)
for item in range(5,10,2):#range(min range, max range,step)
    print(item)
#Eg
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Sum: {total}")