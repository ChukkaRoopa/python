# For the string "I love my India" - reverse only the word "my" and keep the rest as same

string = "I love my India"

for i in range(len(string)):
    if string[i] == "m" and string[i+1] == "y":
        ind = string.index("m")
        list1 = list(string)

        list1[ind], list1[ind+1] = list1[ind +1], list1[ind]
        string = ''.join(list1)
        print(string)