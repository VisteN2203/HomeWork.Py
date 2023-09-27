num = int(input())

if num >= 1:
    for i in range(1, num + 1):
        if i != 1:
            if num % i == 0:
                break

print(i)

