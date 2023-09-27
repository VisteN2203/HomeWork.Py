from math import pow

number = int(input())

flag = True

while number > 10:
    lastNumber = number % 10
    predLastNumber = (number % 100) // 10
    if (lastNumber < predLastNumber or lastNumber == predLastNumber) and flag:
        flag = True
        number //= 10
    else:
        flag = False
        number //= 10

if flag:
    print("YES")
else:
    print("NO")


