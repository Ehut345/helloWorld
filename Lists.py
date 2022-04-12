#Lists or arrays
names = ['John', 'Bob', 'Sarah', 'Mosh', 'Mary']
print(names)#full list
print(names[:])#full list
print(names[0])#1st element in list
print(names[-1])#last element in list
print(names[2:])#for a range in in list
print(names[2:4])#for a range and limit with last excluded in in list
names[0] = 'Jon'
print(names)
#Eg : largest in the list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for x in numbers:
    if x > max:
        max = x;
print(f'the max number is: {max}')