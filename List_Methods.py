#List Methods
numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20)# to add at the end of the list
print(numbers)
numbers.insert(1,13)# to add at the specific loction in the list
print(numbers)
numbers.remove(13)# to remove a number in the list
print(numbers)
numbers.pop()# to remove last one in the list
print(numbers)
print(numbers.index(7))# to check index of the passed number list
print(numbers.count(5))# to count the passed number in the list
#print(numbers.index(13))# if we pass out of list we get error
numbers.sort()#to sort numbers in the list
print(numbers)
numbers.reverse()#to reverse numbers in the list
print(numbers)
numb = numbers.copy()#to copy numbers in the list to another list
numbers.append(10)
print(numb)
print(numbers)
print(13 in numbers)# we get bool output
numbers.clear()# to remove everything in the list
print(numbers)
#Eg : remove duplicats in the list
print('\n')
number = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for num in number:
    if num not in uniques:
        uniques.append(num)
print(uniques)