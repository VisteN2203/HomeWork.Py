x1, y1, x2, y2 = int(input()),int(input()),int(input()),int(input())

x = x1 - x2
y = y1 - y2

if (x1 == x2) or (y1 == y2):
    print("YES")
elif (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0):
    print("YES")
elif (x1 == y1) and (x2 == y2):
    print("YES")
elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
    print("YES")
else:
    print("NO")
