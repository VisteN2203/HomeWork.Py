year = int(input())

calculation1 = (year % 100) // 10
calculation2 = year % 10

if (calculation1 == 0 and calculation2 == 0):
    print("YES")
else:
    print("NO")