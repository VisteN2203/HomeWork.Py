n = int(input())


while n > 999:
	n //= 10

stringN = str(n)

print(stringN[2])
