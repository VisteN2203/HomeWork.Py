from math import pow

a, b = int(input()), int(input())

counter = 0
if a <= b:
    for i in range(a,b + 1):
        cube = pow(i, 3) % 10
        if cube == 4 or cube == 9:
            counter = counter + 1
print(counter)
