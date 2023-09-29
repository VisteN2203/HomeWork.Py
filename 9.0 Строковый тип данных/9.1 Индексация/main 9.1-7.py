text = str(input())

lenText = len(text)
flag = False

for i in range(lenText):
	if text[i] in ("01234567890"):
		flag = True

if flag == True:
	print("Цифра")
else:
	print("Цифр нет")