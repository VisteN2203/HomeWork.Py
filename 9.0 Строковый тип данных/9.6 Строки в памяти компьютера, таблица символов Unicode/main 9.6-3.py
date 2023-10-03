num, string = int(input()), str(input())

for i in string:
	if ord(i) - num < 97:
		print(chr(ord(i) - num + 26),end="")
	else:
		print(chr(ord(i) - num),end="")


