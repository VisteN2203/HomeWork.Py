text = str(input())

textLen = len(text)

if textLen % 2 == 0:
	print(text[textLen // 2:],end="")
	print(text[0:textLen // 2],end="")
else:
	print(text[(textLen // 2) + 1:], end="")
	print(text[0:textLen // 2 + 1], end="")