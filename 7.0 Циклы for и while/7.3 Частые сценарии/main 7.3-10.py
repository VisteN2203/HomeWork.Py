
total = 0

for i in range(10):
    number = int(input())
    if number % 2 == 0:
        total += 1

if total == 10:
    print("YES")
else:
    print("NO")