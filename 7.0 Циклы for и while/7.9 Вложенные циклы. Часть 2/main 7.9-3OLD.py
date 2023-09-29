a, b = int(input()), int(input())

maxNumber = 0
total = 0
maxTotal = -1
maxSum = 0

if a < b:
    for i in range(a, b + 1):
        for j in range(1, b + 1):
            if i % j == 0:
                total += j
                if total >= maxTotal:
                    maxTotal = total
                    maxNumber = i
        total = 0

for k in range(1,maxNumber + 1):
    if maxNumber % k == 0:
        maxSum += k

print(maxNumber, maxSum)