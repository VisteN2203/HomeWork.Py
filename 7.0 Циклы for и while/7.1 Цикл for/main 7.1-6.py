from math import pow

number = int(input())

for i in range(number+1):
    print(f"Квадрат числа {i} равен {int(pow(i, 2))}")
