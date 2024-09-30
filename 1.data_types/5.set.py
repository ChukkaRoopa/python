'''
Set - unordered collection of elements which is iterable, mutable and has no duplicate values.
it is created by using set() function, inside curly braces, separated by a comma.
'''

set1 = set()
print("Black set: ", set1)

set2 = set("Roopa")
print("Set with the use of string: ", set2)

set3 = set(["Roopa", "Age", "Roopa"])
print("Set with the use of list: ", set3)

set4 = set(["Roopa", 1, 2, 4, 3, 'Age', 2])
print("Set with mixed values: ", set4)

set5 = set(("Roopa", "Age", "Roopa"))
print("Set with the use of tuple: ", set5)

set6 = set({1: "leo", "Pet" : "charlie"})
print("Set with the use of dictionary: ", set6)

set7 = {"leo", "leo", "charlie"}
print("creating a set: ",set7)

# Accessing elements of a set
set = set(["Roopa", 1, 2, 4, 3, 'Age', 2, "Age"])
print("Initial Elements in the set: ", set)

for i in set:
    print(i, end = " ")
print("\n")

# Specific value is present in set by using keyword
print("Roopa" in set)
print("Leo" in set)

# adding elements to a set
# add() method
set1.add(3)
set1.add("leo")
set1.add(4)
set1.add((4,5,7))
print("Addition of elements to a set: ", set1)

for i in range(6):
    set1.add(i)
print("Adding of elements: ", set1)

# update() method - accepts lists, strings, tuples
set1.update([9,10])
print("after updation: ", set1)

# removing elements from a set
# remove() / discard()
set1.remove(9)
print("remove method: ", set1)

set1.discard(10)
print("discard of elements: ", set1)

# pop() - If the set is unordered then there’s no such way to determine which element is popped by using the pop() function. 
set1.pop()
print("after poping: ", set1)

# clear() - removes all the elements
set1.clear()
print('removes all the elements: ', set1)