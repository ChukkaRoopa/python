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

# Accessing elements of a set
set = set(["Roopa", 1, 2, 4, 3, 'Age', 2, "Age"])
print("Initial Elements in the set: ", set)

for i in set:
    print(i, end = " ")
print("\n")

# Specific value is present in set by using keyword
print("Roopa" in set)
print("Leo" in set)