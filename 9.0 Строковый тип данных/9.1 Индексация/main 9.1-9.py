text = str(input())

textLen = len(text)
total = 0

for i in range(textLen-1):
	if text[i] == text[i + 1]:
		total += 1

print(total)