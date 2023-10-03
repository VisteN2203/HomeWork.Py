text = str(input())

count = 0

for i in range(0, len(text)):
	for j in range(0, 10):
		if text[i].count(str(j)):
			count += 1

print(count)
