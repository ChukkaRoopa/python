def armstrong(num):

    sum = 0
    for i in str(num):
        sum += int(i) ** 3
    if sum == num:
        return True
    return False

print(armstrong(153))
print(armstrong(1353))
print(armstrong(370))