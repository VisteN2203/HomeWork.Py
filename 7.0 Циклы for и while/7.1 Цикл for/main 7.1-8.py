from math import pow

m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    example = m * pow((1 + (p / 100)), i)
    i += 1
    print(i, example)
