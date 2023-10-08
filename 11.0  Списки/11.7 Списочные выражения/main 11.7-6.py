string = str(input())

list = [int(i) ** 3 for i in string.split()]

print(*list)