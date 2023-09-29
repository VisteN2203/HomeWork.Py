n = int(input())

star = "*"
space = " "

for i in range(1, n + 1):
	if i == 1 or i == n:
		print(star * 19)
	else:
		print(star, space*15, star)