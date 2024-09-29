'''
match-case - it is the switch-case (In python 3.10)
"_" is used as a wildcard when all the cases fails to match the parameter
'''

# Simple match-case statement
def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    match num:
        case 1:
            print("one")
        case 2:
            print("Two")
        case 3:
            print("three")
        case _:
            print("num not between 1 and 3")
runMatch()

# match-case with OR operator
def runMatch():
    num = int(input("Enter a number between 1 and 6: "))
    match num:
        case 1 | 2:
            print("one or two")
        case 3 | 4:
            print("three or four")
        case 5 | 6:
            print("five or six")
        case _:
            print("num not between 1 and 6")
runMatch()

# match-case with if condition
def runMatch():
    num = int(input("Enter a number: "))
    match num:
        case num if num > 0:
            print("positive")
        case num if num < 0:
            print("Negative")
        case _:
            print("Zero")
runMatch()

# match-case with sequence pattern
def runMatch():
    str = "Roopa"
    match str[4]:
        case "a":
            print("case1 matches")
        case "A":
            print("case2 matches")
        case _:
            print("character not present in the string")
runMatch()