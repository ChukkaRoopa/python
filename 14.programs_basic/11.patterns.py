# *
# * *
# * * *
# * * * *
# * * * * *

def pattern1(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end = ' ')
        print()
pattern1(5)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def pattern2(rows):
    for i in range(1,rows+1):
        # for printing spaces
        for j in range(rows - i):
            print(" ", end='')
        # for printing '*'
        for k in range(i):
            print("*",end=' ')
        print()
pattern2(5)

# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

def pattern3(rows):
    for i in range(1, rows + 1):
        num = 1
        for j in range(i):
            print(num, end = ' ')
            num += 1
        print()
pattern3(5)

# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

def pattern4(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end = ' ')
            num += 1
        print()
pattern4(5)

# A
# B B
# C C C
# D D D D
# E E E E E

def pattern5(rows):
    num = 65
    for i in range(1, rows + 1):
        ch = chr(num)
        for j in range(i):
            print(ch, end = ' ') 
        num += 1
        print()      
pattern5(5)

# A
# B C
# D E F
# G H I J
# K L M N O

def pattern6(rows):
    num = 65
    for i in range(1, rows + 1):
        for j in range(i):
            ch = chr(num)
            print(ch, end = ' ')
            num += 1
        print()
pattern6(5)