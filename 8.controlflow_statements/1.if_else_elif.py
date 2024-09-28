# if-statement
if 10 > 5:
    print("10 is greater than 5.")
print("Program ended")

# if-else
x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

# nested if-else
num = 6
if num == 3:
    print("num is 3")
else: 
    if num == 2:
        print("num is 2")
    else:
        if num == 5:
            print("num is 5")
        else:
            print("num is not present")

# nested if
num = 6
if num > 5:
    print("num is greater than 5")
    if num < 10:
        print("num is in between 5 and 10")

# if-elif-else
num = 6
if num == 3:
    print("num is 3")
elif num == 2:
    print("num is 2")
elif num == 6:
    print("num is 6")
else:
    print("num is not present")