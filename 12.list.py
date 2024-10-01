# list - list is just like arrays, which is an ordered collection of elements. Square brackets []
list1 = []
print("Empty list: ", list1)

list2 = ["Roopa"]
print("list with use of a string: ", list2)

list3 = ["Roopa", "Age", 23]
print("List with multiple values: ",list3)

list4 = [["Roopa", "Age"], "Phone number"]
print("Muliti-dimension list: ", list4)

# Accesing items of a list
print("accessing list items: ", list4[0][1])

print(list4[-2][1])

# size of the list
print("size of the list: ", len(list4))

# taking input of a list
#example
# string = input("enter elements space separated: ")
# list1 = string.split()
# print(list1)

# example
# n = int(input("Enter the size of list: "))

# lst = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
# print(lst)

# adding elements to a list
list1 = []

# append() method - only one element can be added 
list1.append(6)
list1.append("Roopa")
print("adding elements using append() method: ",list1)

# we can add multiple values using append() by using loop
for i in range(1,4):
    list1.append(i)
print("adding mltiple elements using append() method",list1)

# addition of list to a list
list2 = ["leo", "Charlie"]
list1.append(list2)
print("addition of list to a list: ",list1)

# insert() method - addition of elements at desired position
list1.insert(2,"roopa")
print("addition of elements using insert() method: ",list1)

# extend() method - addition of multiple elements at the end of the list
list1.extend([2,6,7,8])
print("addition of elements using extend() method: ",list1)

# reversing a list
list1.reverse()
print("reverse a list using reverse() method: ", list1)

list3 = ["Roopa", "Age", 23]
lst = list(reversed(list3))
print("reverse a list using reversed() function: ", lst)

# remove elements from the list
# remove() method - removes only one element
list1.remove(3)  # pass the element as a argument
print("list after remove() method: ", list1)

# pop() method
list1.pop() # removes the last element of the list
print("list after pop() method: ", list1)

list1.pop(2)  # here 2 is the index of the list
print("list after pop() method: ", list1)

# Slicing of a list
list1 = ['R', 'o', 'o', 'p', 'a', 'c', 'h', 'u', 'k', 'k', 'a']
#index    0    1    2    3    4    5    6    7    8    9    10
#-ve_ind  -11  -10  -9  -8   -7   -6   -5   -4   -3   -2    -1

sliced_list = list1[3:8]     # will exclude the value of 8th index
print("Slicing elements in a range 3-8: ", sliced_list)

sliced_list = list1[4:]
print("Slicing from 4th index to end: ", sliced_list)

sliced_list = list1[:]
print("priting all elements using slicing: ", sliced_list)

# negative index list slicing
sliced_list = list1[:-6]
print("elements sliced till 6th element from last: ", sliced_list)

sliced_list = list1[-6:-1]
print("Slicing from index -6 to -1: ", sliced_list)

sliced_list = list1[::-1]
print("printing list in reverse order: ", sliced_list)

# list comprehension
list1 = [i*5 for i in range(1,11) if i % 2 == 0]
print("List comprehension: ", list1)

# functions
list1 = [1,2,4,3,5,6,7,1,2,9]

print("sum: ",sum(list1))

#count()
print("count: ",list1.count(2))

#len()
print("length of the list: ",len(list1))

# index()
print("index of the element 2 is: ",list1.index(2))

print("index of the element 2 after 4th index is: ",list1.index(2,4))

#min()
print("min value in the list: ",min(list1))

#max()
print("max value in the list: ",max(list1))

# sort
list1.sort()
print("Sorted list: ",list1)

# in descending order
list1.sort(reverse=True)
print("Sorted list in descending order: ",list1)

# using reverse() function
list1 = [1,2,4,3,5,6,7,1,2,9]
list1.reverse()
print("reverse list: ",list1)

# Deletion of elements
# pop() method
list1.pop()
print("pop() method: ",list1)

list1.pop(0)
print("pop() method: ",list1)

# del() method
del list1[1]
print("delete element from the list: ",list1)

# remove() - remove element using name/value
list1.remove(6)
print("remove method: ", list1)

# nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]
print("nested list comprehension: ",matrix)