num = int(input())
list = []

for i in range(num):
	text = str(input())
	if not text in list:
		list.append(text)

print(*list, sep="\n")
