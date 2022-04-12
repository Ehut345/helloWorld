#Return Statement
def square(number):
    return number*number
num = square(4)
print(num)
print(square(3))
#if we don't return
def square(number):
    print(number*number)
print(square(3))#we get none expection