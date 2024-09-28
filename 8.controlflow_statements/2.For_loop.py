# For loop with string
string = "Roopa"
for i in string:
    print(i)

# for loop with range
for i in range(0,10,2):   # start, stop(not included), step size
    print(i)

# for loop enumerate() - keep track of iterables as well as index
items = ["apple", "orange", "grapes"]
for index, item in enumerate(items):
    print(index, item)

# nested for loops
for i in range(1,4):
    for j in range(1, 4):
        print(i, j)

# for loop over list
items = ["apple", "orange", "grapes"]
for item in items:
    print(item)

# for loop in one line
num = [i for i in range(10)]
print(num)

# for loop with dictionary
dict = dict({1 : "leo", 2 : "Charlie"})
for i in dict:
    print(i, dict[i])

# for loop with tuple
t = ((1, 2), ("Roopa", "name"), ("x", 3))
for a, b in t:
    print(a, b)

# for loop with zip() - used to iterate over two lists in parallel
fruits = ["apple", "banana"]
colours = ["red", "yellow"]
for fruit, colour in zip(fruits, colours):
    print(fruit,"is",colour)

# continue in For loop - coninue - returns the control to the beginning of the loop
string = "Roopa"
for i in string:
    if i == "o" or i == "a":
        continue
    print("current letter: ",i)

# break in for loop
string = "Roopa"
for i in string:
    if i == "o" or i == "a":
        break
    print("current letter: ",i)

# For loop with Pass statement
for i in "Roopa":
    pass