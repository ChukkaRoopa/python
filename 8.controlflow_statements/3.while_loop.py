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