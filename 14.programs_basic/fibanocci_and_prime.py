import math
def is_prime(num):
    if num in [2,3]:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(num)),2):
        if num % i == 0:
            return False
    return True

a = 0
b = 1
series = []

for i in range(10):
    
    if is_prime(a):
        series.append(a)
    temp = a + b
    a = b
    b = temp

print(series)