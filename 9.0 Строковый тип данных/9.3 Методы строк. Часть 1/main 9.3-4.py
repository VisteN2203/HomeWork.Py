text = str(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
total = 0

for i in range(0,len(text)):
	if text[i] in alphabet:
		total += 1

print(total)