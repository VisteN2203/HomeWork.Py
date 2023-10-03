text = str(input())

for i in range(0,len(text)):
	if i % 3 != 0:
		print(text[i],end="")