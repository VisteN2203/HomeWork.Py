from multiprocessing import *

num = int(input())

total = 1

while num != 0:
    remains = num % 10
    total = remains * total
    num //= 10
print(total)




# Прошлый код
# n = input()
# product = n % 10
# while n >= 10:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)