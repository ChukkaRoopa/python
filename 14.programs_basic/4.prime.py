import math
def prime(num):
    if num in [2,3]:
        return True
    if num == 0 or num % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(num)),2):
        if num % i == 0:
            return False
    return True

print(prime(79))