num = str(input())

list = (num.split())
list = [int(x) for x in list]

list.sort()
print(*list)

list.sort(reverse=True)
print(*list)