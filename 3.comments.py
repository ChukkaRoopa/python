# I'm a single line comment

# Python multi-line comments
# multiline comments

# string - literals :- Python ignores string literals that are not assigned to a variable
'this is a string literal which is not assigned and it is ignored'

'''This is multiline comments
using string literals'''

# Doc - string :- It is the string literal with triple quotes that appear right after the function.
def multiply(a, b):
    """Multiples the value of a and b"""
    return a*b
print(multiply.__doc__)