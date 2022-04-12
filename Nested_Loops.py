#Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
#Eg :how to print F
print('\n')
numbers = [5,2,5,2,2]
for x in numbers:
    print("x" * x)
#nested loop for F
numbers = [5,2,5,2,2]
print('\n')
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)
#nested loop for L
numbers = [2,2,2,2,5]
print('\n')
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)