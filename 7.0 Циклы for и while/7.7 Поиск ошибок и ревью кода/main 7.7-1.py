
count = 0
total = 1

for i in range(1, 11):
    x = int(input())
    if x >= 0:
        count += 1
        total *= x

if count != 0:
     print(count,total,sep="\n")
else:
     print('NO')