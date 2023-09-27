from math import factorial

n = int(input())

# if n <= 12:
#     print(factorial(n))

number = 1
for i in range(1,n + 1):
    number = i * number
print(number)
