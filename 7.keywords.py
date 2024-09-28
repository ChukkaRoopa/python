'''
keywords - keywords are the reserved words that cannot be used as a variable, identifier or a function name.
'''

# get all the list of keywords
import keyword
print("Keywords: ", keyword.kwlist)

# Note - None is not equal to 0 or ann empty list [], It denotes void or null.

# in 
for i in "Leo":
    print(i, end = " ")

print()
# is 
print(' ' is ' ')   # it checks if two strings are equal - returns True
print({ } is { })    # checks if two dictionaries are equal - returns False

# For, while, break, continue 
for i in range(10):
    print(i, end = " ")
    if  i == 6:
        break

print()
i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end = ' ')
    i += 1
print()

# if, else, elif
i = 50
if i == 5:
    print("i is 5")
elif i == 10:
    print("i is 10")
else:
    print("i is not present")

# def, class, with, as, pass, lambda
# def
def fun():
    print("def keyword in python.")
fun()

#class
class Dog():
    attr1 = "dog"
    attr2 = "pet"
    def fun(self):
        print("I'm a ",self.attr1)
leo = Dog()
leo.fun()
print(leo.attr2)

# with
with open('/Users/roopachukka/Documents/python/7.with_file.py', 'w') as with_file:
    with_file.write("Hello world!!")

# as - used to create an alias for the module imported
import math as roopa
print("as keyword in python",roopa.factorial(5))

# pass - pass is a null statement. nothing happens when it is encountered. it is used to prevent indentation errors and placeholders
for i in range(10):
    pass

# lambda
g = lambda x: x*x*x*x
print("lambda function: ",g(2))

# return , yield
# return - is used to return from the function
def fun():
    s = 0
    for i in range(10):
        s += i
    return s
print(fun())

# yield - is used as a return but is used to return a generator
def fun():
    s = 0
    for i in range(10):
        s += i
    yield s
print(fun())

# import, from
from math import factorial
print(factorial(5))

import math
print(math.factorial(5))

# exception handlingg keywords - try, except, raise, finally, and assert
a = 5
b = 0
try:
    print(a//b)
except ZeroDivisionError:
    print("Cannot divide by zero")

assert b != 0, "Divide by 0 error"

var = "Roopa"
if var != "leo":
    raise TypeError("Both the strings are different.")

# del
a = 10
print(a)

del a
print(a)