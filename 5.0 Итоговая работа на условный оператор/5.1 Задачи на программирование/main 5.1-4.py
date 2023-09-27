num = int(input())

i = "I"
v = "V"
x = "X"
if num == 1:
    print(i)
elif num == 2:
    print(i*2)
elif num == 3:
    print(i*3)
elif num == 4:
    print(i+v)
elif num == 5:
    print(v)
elif num == 6:
    print(v+i)
elif num == 7:
    print(v+i*2)
elif num == 8:
    print(v+i*3)
elif num == 9:
    print(i+x)
elif num == 10:
    print(x)
else:
    print("ошибка")
