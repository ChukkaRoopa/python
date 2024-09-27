'''
variables - variable is container to store values.
'''

# declaration and initialization of variables
var = "Leo"
var1 = 63
print(var, var1)

# re-declaring variables
number = 10
print("before declaration: ", number)
number = 12
print("after declaration: ", number)

# assign values to multiple variables
a = b = c = 10
print("assign values to multiple variables",a, b, c)

# Assigning different values to multiple variables
a, b, c = 10, "Leo", "Charlie"
print("assign different to multiple variables",a, b, c)

# "+" operator
a, b = 5, 10
print("+ operator: ", a + b)

a, b = "Leo", "Charlie"
print("+ operator: ", a + b)

# Note  -  "+" operator for different data types produces an error
a, b = 10 , "leo"
#print("+ operator: ", a + b)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Local variable - declared inside the function, cannot be called outside the function
def fun():
    s = "leo"
    print("local variable: ",s)
fun()

# Global variable - declared outside the function, can be accessed inside the function
s = "Charlie"
def fun():
    print("Global variable: ",s)
fun()

# Global keyword
x = 5
def fun():
    global x
    x = x - 2
    print("Value of x inside function: ", x)
fun()
print("Value of x outside function: ", x)