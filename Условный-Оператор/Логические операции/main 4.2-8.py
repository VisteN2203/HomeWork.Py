y1,x1,y2,x2 = int(input()),int(input()),int(input()),int(input())

x = x1 - x2
y = y1 - y2

if (x == 1 or x == -1 or x == 0) and (y == 1 or y == -1 or y == 0):
    print("YES")
else:
    print("NO")