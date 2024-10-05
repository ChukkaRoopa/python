def fibanocci(num):
    a = 0
    b = 1
    res = []
    for i in range(num):
        res.append(a)
        temp = a + b
        a = b
        b = temp
    return res

print(fibanocci(10))