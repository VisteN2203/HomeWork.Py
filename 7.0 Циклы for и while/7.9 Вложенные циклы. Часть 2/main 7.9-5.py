n = int(input())

while n > 9:
	sum = 0
	while n > 0:
		lastDigit = n % 10
		sum += lastDigit
		n //= 10
	n = sum
print(n)