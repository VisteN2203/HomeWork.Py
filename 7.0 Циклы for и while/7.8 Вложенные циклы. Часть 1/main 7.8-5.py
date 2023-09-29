number = int(input())

napas = number // 2

for i in range(1,number+1):
    for j in range(i):
        print(i,end="")
    print()


