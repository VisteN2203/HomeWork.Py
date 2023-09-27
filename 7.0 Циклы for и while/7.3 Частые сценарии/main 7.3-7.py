n = int(input())
numbers = 0

for i in range(1,n + 1):
    if n % i == 0:
        numbers += i
print(numbers)