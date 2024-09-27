'''
input() - It takes the input from the user and converts into a string. The type will always be a '<class 'str'>'
'''

num = input("Enter a number: ")
print(num, " ", type(num))

char = input("Enter a character: ")
print(char, " ", type(char))

num = int(input("Enter a number: "))
print(num, " ", type(num))

num = float(input("Enter a number: "))
print(num, " ", type(num))