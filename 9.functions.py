# creating a function
def fun():
    print("Welcome")

# calling a function
fun()

# function with parameters
def fun(num1:int, num2:int) -> int:
    num3  = num1 + num2
    return num3
ans = fun(2,3)
print(ans)

# fun to check prime numbers
import math
def is_prime(n):
    if n in [2,3]:
        return True
    if n == 1 or n % 2 == 0:
        return False
    r = 3
    while r <= math.sqrt(n):
        if n  % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

# fun arguments
def evenOdd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
evenOdd(5)
evenOdd(6)

# default arguments
# parameter - variable defined within parathesis during function definition
def fun(x, y = 10):
    print("x: ", x)
    print("y: ", y)
# Arguments - values passed to the function when it is called.
fun(40)

# keyword argument
def fun(firstname, lastname):
    print(firstname, lastname)
fun(firstname="Roopa", lastname="Chukka")
fun(lastname="Chukka", firstname="Manohar")

# positional arguments
def fun(name, age):
    print(f"Hi my name is {name}. I'm {age} years old.")
fun("Roopa", 23)
fun(23,"roopa")  # will get incorrect output, bcz arguments are not in order

# arbitrary keyword arguments
# *args() - non-keyword arguments
# **kwargs() - keyword arguments

# variable length non-keyword arguments
def fun(*args):
    for i in args:
        print(i)
fun("Hello", "Good", "morning.")

# variable length key-word arguments
def fun(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
fun(a ="Roopa", b = "manohar")

# Docstring - First string after the function is called is called Document string or Docstring.
def evenOdd(n):
    """function to check the number is even or odd"""
    if n % 2 == 0:
        print("even")
    print("odd")
print(evenOdd.__doc__)

# Function within functions
def f1():
    s = "Roopa"
    def f2():
        print("Function within functions: ",s)
    f2()
f1()

# Anonymous functions - function without a name
def cube(x): return x*x*x
print(cube(3))

# recursive function - function calls itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)
print(factorial(5))

# return statement - used to exit from the function and go back to the function caller and return the specific value from the caller.

# swapping
def swap(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)
print(swap(2,3))

# lambda function
str = "Roopa"
x = lambda string: string.upper()
print(x(str))

# condition checking using lambda function
x = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:.2f}"

print(x(123))
print(x(23.45))

# lambda function with list comprehension
x = [lambda arg = y: arg* 10 for y in range(1, 5)]
for i in x:
    print(i())

# 