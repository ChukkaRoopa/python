def factorial(num):
    
    if num == 0:
        return 1
    fact = 1
    for i in range(1,num+1):
        fact = i * fact
    return fact

print(factorial(5))