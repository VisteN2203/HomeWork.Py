text = str(input())

textLen = len(text)
totalGlas = 0
totalSoglas = 0

for i in range(textLen):
	if text[i] in "ауоыиэяюёеАУОЫИЭЯЮЁЕ":
		totalGlas += 1
	if text[i] in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
		totalSoglas += 1

print(f"Количество гласных букв равно {totalGlas}")
print(f"Количество согласных букв равно {totalSoglas}")

