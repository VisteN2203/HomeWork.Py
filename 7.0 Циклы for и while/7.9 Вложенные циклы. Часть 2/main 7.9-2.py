

n = int(input())

total = 1

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end="")

    for k in range(j, 1, -1):
        print(k - total, end="")
    print()
