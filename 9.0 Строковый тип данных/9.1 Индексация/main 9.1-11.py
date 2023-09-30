num = int(input())

s = ""

while num != 0:
	s += str(num % 2)
	num //= 2

for i in range(-1, -len(s)-1, -1):
	print(s[i],end="")