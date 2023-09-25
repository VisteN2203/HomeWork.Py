n = int(input())

number = 0
if n <= 100:
    for i in range(1, n + 1):
       number = i + number
    print(number)
print(number)

