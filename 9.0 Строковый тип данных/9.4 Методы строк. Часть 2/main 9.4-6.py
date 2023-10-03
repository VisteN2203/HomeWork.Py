text = str(input())

number = 0
Letter = ""

for i in text:
	if text.count(i) >= number:
		number = text.count(i)
		Letter = i
print(Letter)
