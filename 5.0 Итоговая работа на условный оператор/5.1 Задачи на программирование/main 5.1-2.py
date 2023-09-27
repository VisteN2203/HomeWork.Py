x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())


if (x1 % 2 == 0) == (x2 % 2 == 0):
    if (y1 % 2 == 0) == (y2 % 2 == 0):
        print("YES")
    else:
        print("NO")
else:
    print("YES")