num = int(input())

s = 0

while num > 0:
    if num % 2 == 0:
        s += num % 10
    num //= 10
print(s)