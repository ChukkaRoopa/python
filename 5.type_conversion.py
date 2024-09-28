'''
Python defines type conversion functions which directly converts one data type to another.
1. Implicit type conversion
2. Explicit type conversion
'''

# Implicit type conversion - python intrepreter automatically converts one data type to another without user involvement.
x = 10
print("x is of type: ", type(x))
y = 19.56
print("y is of type: ", type(y))
z = x + y 
print("z is of type: ", type(z))
print(z)

# Explicit type conversion - data type is manually changed by the user as per the requirement.
# int(a, base) - converts data type into integer. Base specifies the base in which the string is if the data type is string.
a = "101"
print("After converting to integer base 2: ", int(a, 2))

print("After converting to float: ", float(a))

# ord() - convert character to integer
b = '4'
print("converting character to integer: ", ord(b))

print("converting integer to hexadecimal: ", hex(55))

print("converting integer to octal: ", oct(55))

# Type conversion using tuple(), set(), list()
string = "Roopa"

print("converting string to tuple: ", tuple(string))

print("converting string to set: ", set(string))

print("converting string to list: ", list(string))

# Type conversion using dict(), complex(), str()
a = 1
b = 2
print("Convert integer to complex: ", complex(a, b))

print("Convert integer to string: ", str(a))

tup = ((1, "r"), ("r", "s"))
print("Convert tuple to dict: ", dict(tup))

# convert ASCII values to characters
a = chr(99)
print(a)