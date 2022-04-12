#double couts
course = "Python's course for beginners"
print(course)
#single couts
course = 'Python for "beginners"'
print(course)
#multi lines 3 couts
course = '''
Hi John,

Here is our first email to you

Thank you,
The support team

'''
print(course)
#index of a string
course = 'Python for beginners'
print(course[-1])#we can even use -ve index in python
#index of a string
course = 'Python for beginners'
print(course[0:3])#we can use for a range, o/t : 'Pyt'
#index of a string
course = 'Python for beginners'
print(course[1:])#if we don't mention end index, o/t : 'ython for beginners'
#index of a string
course = 'Python for beginners'
print(course[:5])#if we don't mention start index, o/t : 'Pytho'
#copy of a string
course = 'Python for beginners'
another = course[:]#if we don't mention start and end index
print(another)
#
name = "Jennifer"
print(name[1:-1])