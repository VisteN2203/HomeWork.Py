text = str(input())

textLen = len(text)
totalPlus = 0
totalStar = 0

for i in range(textLen):
	if text[i] in ("+"):
		totalPlus += 1
	if text[i] in ("*"):
		totalStar += 1

print(f"Символ + встречается {totalPlus} раз")
print(f"Символ * встречается {totalStar} раз")