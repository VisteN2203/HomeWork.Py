numbers = int(input())

Hihihi = numbers
flag = True
num = Hihihi % 10

while numbers != 0:
    if flag == True:
        remains = numbers % 10
        if num == remains:
            flag = True
        else:
            flag = False
        numbers //= 10
    else:
        numbers //= 10

if flag == True:
    print("YES")
else:
    print("NO")