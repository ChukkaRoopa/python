# Syntax error
amount = 10000
if (amount > 9000)
print("You are eligile for a voucher.")

# ZeroDivisonError
marks = 10
a = marks / 0
print(a)

# TypeError
x = 5
y = "Roopa"
z = x + y

# try catch block to resolve it
x = 5
y = "Roopa"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and str")

# Example
list1 = [1,2,4]
try:
    print(list1[3])
    print(list1[6])
except:
    print("an error occured.")

# Try with else clause
def fun(a,b):
    try:
        c = (a + b) / (a - b)
    except ZeroDivisionError:
        print("cannot divide by 0")
    else:
        print(c)
fun(3,3)
fun(4,5)

# finally keyword - it is always executed after the try and except blocks
a = 5
try:
    b = a / 0
except ZeroDivisionError:
    print("DIvide by 0 error")
finally:
    print("this is always executed.")

# raise exception - allows programmer to force a specific exception to occur
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("An exception")
    raise