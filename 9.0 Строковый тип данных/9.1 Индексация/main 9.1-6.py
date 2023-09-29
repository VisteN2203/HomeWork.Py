num = int(input())

len = len(str(num))

total = 0

for i in range(1,len + 1):
	lastDigit = num % 10
	total += lastDigit
	num //= 10
print(total)

