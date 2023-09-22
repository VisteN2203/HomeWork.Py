data = int(input())

if data == 2:
    print(28)
elif (data < 7 and data % 2 == 0) or (data % 2 != 0 and data > 7):
    print(30)
else:
    print(31)
