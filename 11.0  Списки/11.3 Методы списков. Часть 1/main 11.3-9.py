num = int(input())
list = []

for i in range(num):
	text = str(input())
	for j in range(len(text)):
		list.append(text[j])

print(list)