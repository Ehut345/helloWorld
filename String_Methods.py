#all string function doesn't affect original string
course = 'Python for Beginners'
print(len(course))#len for counting for length of string
print(course.upper())#pritns all in uppercase doesn't change original string
print(course)
print(course.lower())#pritns all in lowercase
print(course.find('o'))
print(course.find('O'))#if we pass non excting letter vwe get -1
print(course.find('Beginners'))
print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('beginners','Absolute Beginners'))#if it can't find the word it will print original string
print(course.replace('P','J'))
print('Python' in course)#returns bool : true
print('python' in course)#returns bool : flase
print(course.title())#returns a string where the first character in every word is upper case