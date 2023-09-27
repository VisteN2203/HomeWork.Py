from math import pow

pow = int(pow(10, 6))

total = 0

for i in range(7):
    x = int(input())
    if -pow <= x <= pow:
        if x % 2 == 0:
            total += x
print(total)

# Прошлый код
# s = 1
# for i in range(1, 7):
#     n = input()
#     if i % 2 == 0:
#         s = s + n
# print(s)