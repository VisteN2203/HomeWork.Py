from math import pow

n = int(input())

numbers = 0
for i in range(1,n+1):
    total = (pow(i, 2)) % 10
    if total == 5:
        numbers += i
print(int(numbers))