# while loop
count = 0
while count < 4:
    print("While loop")
    count += 1

# Infinite while loop
# count = 0
# while count < 4:
#     print("Infinite loop")  # runs infinte times

# While with contine statement
string = "Roopa"
n = len(string)
i = 0
while i < n:
    if string[i] == "o":
        i += 1
        continue
    print("current char: ",string[i])
    i += 1

# while loop with break statement
string = "Roopa"
n = len(string)
i = 0
while i < n:
    if string[i] == "o":
        i += 1
        break
    print("current char: ",string[i])
    i += 1

# while loop with a pass statement
var = "Roopa"
i = 0
while i < len(var):
    i += 1
    pass

# sentinel controlled statement - we don't know how many times loop will execute, for this we use a sentinel value
# generally the sentinel value is -1, whenever user enters it loop will not execute
a = int(input("enter a number (-1 will terminate the loop): "))
while a != -1:
    a = int(input("enter a number (-1 will terminate the loop): "))

# while loop with boolean values
i = 0
while True:
    i += 1
    print("Count is: ",i)
    if i == 5:
        break
print("Loop has ended.")

# while loop with list
list = [1,2,3,4,5]
while list:
    print(list.pop())